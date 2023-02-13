

function Services() {
     // Get the "See more" link and the hidden content
  const moreLink = document.querySelector('.more-link');
  const moreText = document.querySelector('.more-text');
  const intro = document.querySelector('.intro');

  // Add a click event listener to the "See more" link
  moreLink.addEventListener('click', (event) => {
    // Prevent the link from following the href
    event.preventDefault();

    // Toggle the "show-more" class on the description element
    const description = document.querySelector('.description');
    description.classList.toggle('show-more');

    // Toggle the "hidden" class on the intro paragraph
    intro.classList.toggle('hidden');

    // Change the link text depending on the state
    if (description.classList.contains('show-more')) {
      moreLink.textContent = 'See less';
    } else {
      moreLink.textContent = 'See more';
    }
  });
}
