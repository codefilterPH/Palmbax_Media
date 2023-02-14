from django.db import models
# Tools
from django.utils.translation import gettext_lazy as _
from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
)
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet

# wagtail API
from wagtail.api import APIField


class AboutPage(Page):
    max_count = 1
    parent_page_types = [
        'home.HomePage',
    ]
    subpage_types = [
        'about.PeoplePage',
        'about.AnalyticSettings',
        'about.Clients',
        'about.Testimonials',
    ]

    template = 'about/about_page.html'

    details = RichTextField(_('Company Details'),
                            max_length=1000,
                            blank=True,
                            features=['bold'],
                            help_text='Enter your company narrative details.')

    cover_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Background image. Best size for this image will be 1400x500",
    )

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.RelatedFields('why_choose_us', [
            index.SearchField('title'),
            index.SearchField('text'),
        ])
    ]

    api_fields = [
        APIField('details'),
        APIField('cover_photo'),
        APIField('why_choose_us'),
        APIField('analytics'),
        APIField('clients'),
        APIField('date'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('cover_photo'),
            FieldPanel('details'),
            InlinePanel('why_choose_us', label='Why choose us'),
        ], heading='About Us Information')
    ]

    class Meta:
        verbose_name = 'About Us Page'
        verbose_name_plural = 'About Us Page'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['live_page_status'] = AboutPage.objects.live().exists()
        context['live_people_status'] = PeoplePage.objects.live().exists()
        all_emp = PeoplePage.objects.live()
        paginator = Paginator(all_emp, 3)
        page = request.GET.get("page")
        try:
            context['people'] = paginator.page(page)
        except PageNotAnInteger:
            context['people'] = paginator.page(1)
        except EmptyPage:
            context['people'] = paginator.page(paginator.num_pages)

        return context


class WhyChooseUs(Orderable):
    page = ParentalKey(
        'AboutPage',
        on_delete=models.CASCADE,
        related_name='why_choose_us'
    )

    text = models.TextField(_('Enter your reason'),
                            null=True,
                            blank=False,
                            help_text='Please enter your reasons.')

    panels = [
        FieldPanel('text'),
    ]

    class Meta:
        verbose_name = 'WHY CHOOSE US?'
        verbose_name_plural = 'WHY CHOOSE US?'


@register_snippet
class CompanyRole(models.Model):
    role_name = models.CharField(_('Staff or Employee Role Name'),
                                 max_length=255,
                                 null=True,
                                 help_text='Ex: CEO, Manager, Graphic Designer and etc.')

    def __str__(self):
        return self.role_name


class PeoplePage(Page):
    parent_page_types = [
        'about.AboutPage',
    ]
    template = 'about/people_page.html'
    profile = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(_('Employee/Staff Name'),
                            max_length=50,
                            null=True,
                            blank=False,
                            help_text='Type the name of the person.')
    role = models.ForeignKey(CompanyRole,
                             null=True,
                             on_delete=models.SET_NULL)
    details = RichTextField(_('Details'),
                            null=True,
                            blank=False,
                            help_text='Please person\'s best description.')
    feature = models.BooleanField(_('Feature To Home'),
                                  default=False,
                                  )

    search_fields = Page.search_fields + [
        index.SearchField('name'),
    ]

    api_fields = [
        APIField('profile'),
        APIField('name'),
        APIField('role'),
        APIField('details'),
        APIField('feature'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('profile'),
            FieldPanel('name'),
            FieldPanel('role'),
            FieldPanel('details'),
            FieldPanel('feature'),
        ], heading='Profiles')
    ]

    class Meta:
        verbose_name = 'Staff and Employee'
        verbose_name_plural = 'Staff\'s and Employees'


class Analytics(Page):
    """Subpage from about page"""
    template = 'about/analytics_page.html'
    parent_page_types = [
        'about.AnalyticSettings',
    ]

    value = models.PositiveSmallIntegerField(_('Analytic Value'),
                                             null=True,
                                             blank=False,
                                             help_text='Enter the whole number value 1-100+'
                                             )
    field = models.CharField(_('Field Name'),
                             max_length=40,
                             null=True,
                             blank=False,
                             help_text='Enter the field name. ex: \"Number of clients\".')

    search_fields = Page.search_fields + [
        index.SearchField('field'),
    ]

    api_fields = [
        APIField('field'),
        APIField('value'),
    ]

    class Meta:
        verbose_name = _('Analytic Entry Page')
        verbose_name_plural = _('Analytic Entry Pages')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('field'),
            FieldPanel('value'),
        ], heading='Analytics')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['analytics'] = Analytics.objects.live().order_by('first_published_at')

        return context


class AnalyticSettings(Analytics):
    parent_page_types = [
        'about.AboutPage',
    ]
    subpage_types = [
        'about.Analytics',
    ]

    max_count = 1;
    template = "about/analytics_page.html"

    analytics_background_img = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Background image. Best size for this image will be 1400x400",
    )

    class Meta:
        verbose_name = _('Analytic Setup Page')
        verbose_name_plural = _('Analytics Setup Page')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('analytics_background_img'),
        ], heading='Analytic Page Setup'),
        MultiFieldPanel([
            FieldPanel('field'),
            FieldPanel('value'),
        ], heading='Analytics First Entry')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['analytics'] = Analytics.objects.live().order_by('first_published_at')

        return context


class Clients(Page):
    """Subpage from about page"""
    template = 'about/clients_page.html'
    parent_page_types = [
        'about.AboutPage',
    ]

    name = models.CharField(_('Client\'s Name'),
                            max_length=50,
                            null=True,
                            blank=False,
                            help_text='Enter the client\'s business name.'
                            )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    date = models.DateTimeField(auto_now_add=True, null=True)

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('image'),
        index.SearchField('date'),
    ]

    api_fields = [
        APIField('name'),
        APIField('image'),
        APIField('date'),
    ]

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('image'),
        ], heading='Clients')
    ]


class Testimonials(Page):
    """People will send their testimony from the front end"""
    template = 'about/testimonials_page.html'
    parent_page_types = [
        'about.AboutPage',
    ]

    name = models.CharField(_('Your name'),
                            max_length=50,
                            null=True,
                            blank=False,
                            help_text='Enter the client\'s business name.'
                            )

    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    testimony = models.TextField(_('Testimony'),
                                 max_length=2000,
                                 null=True,
                                 blank=False,
                                 help_text='Input your narrative speech.'
                                 )

    date = models.DateTimeField(auto_now_add=True, null=True)

    search_fields = Page.search_fields + [
        index.SearchField('name'),
    ]

    api_fields = [
        APIField('name'),
        APIField('profile_image'),
        APIField('testimony'),
        APIField('date'),
    ]

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('profile_image'),
            FieldPanel('testimony'),
        ], heading='Testimonial(s)')
    ]
