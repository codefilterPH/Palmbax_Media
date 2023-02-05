
//keep the selection on a navigation bar item when it's clicked except home
const navbar = document.querySelector("#navbar");
const click_links = navbar.querySelectorAll("a");

// Function to handle the selection of a navbar item
function selectItem(event) {
  // Remove the selected class from all items
  click_links.forEach(link => link.classList.remove("selected"));
  // Add the selected class to the clicked item, but only if the page is not "Home"
  if (event.target.innerText !== "Home") {
    event.target.classList.add("selected");
    // Save the selected item in local storage
    localStorage.setItem("selectedNavbarItem", event.target.innerText);
  } else {
    // Remove the selected item from local storage
    localStorage.removeItem("selectedNavbarItem");
  }
}

// Attach the click event to each navbar item
click_links.forEach(link => link.addEventListener("click", selectItem));

// Check if a selected item was saved in local storage
const selectedItem = localStorage.getItem("selectedNavbarItem");
if (selectedItem && location.pathname !== "/") {
  // If a selected item was saved and the page is not "Home", find it in the navbar and add the selected class
  const selectedLink = Array.from(click_links).find(link => link.innerText === selectedItem);
    if (selectedLink) {
        selectedLink.classList.add("selected");
    }
}


// Get all the footer links
const footerLinks = document.querySelectorAll('#footer');
const footer = footerLinks[0];
const click_links2 = footer.querySelectorAll("a");

// Get the header navigation list
const headerNavList = document.getElementById('navbar');

// Loop through the footer links and add click event listeners
click_links2.forEach((link, index) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();

    // Get the corresponding header navigation link
    const headerNavLink = headerNavList.querySelectorAll('a')[index];

    // Trigger a click event on the header navigation link
    headerNavLink.click();
  });
});
