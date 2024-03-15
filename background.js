function updateParallax() {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    var parallaxFactor = -0.5; // Adjust this value to control the intensity of the parallax effect
    var backgroundOffset = scrollTop * parallaxFactor;
    document.querySelector('.background').style.backgroundPositionY = backgroundOffset + 'px';
    
    requestAnimationFrame(updateParallax);
  }

  updateParallax();