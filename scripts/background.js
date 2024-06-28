// background.js

class ParallaxBackground {
  constructor(selector, parallaxFactor = -0.5) {
    this.element = document.querySelector(selector);
    this.parallaxFactor = parallaxFactor;
    this.updateParallax = this.updateParallax.bind(this);
    this.init();
  }

  init() {
    if (!this.element) {
      console.error(`Element not found with selector: ${this.selector}`);
      return;
    }
    window.addEventListener('scroll', this.updateParallax);
    this.updateParallax(); // Initial call to set the position
    this.addSmoothScrolling();
  }

  updateParallax() {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const backgroundOffset = scrollTop * this.parallaxFactor;
    this.element.style.backgroundPositionY = `${backgroundOffset}px`;

    requestAnimationFrame(this.updateParallax);
  }

  addSmoothScrolling() {
    let currentScroll = window.scrollY;
    let targetScroll = window.scrollY;
    let isScrolling = false;

    const smoothScroll = () => {
      if (currentScroll !== targetScroll) {
        currentScroll += (targetScroll - currentScroll) * 0.1; // Smooth scroll factor
        window.scrollTo(0, currentScroll);
        requestAnimationFrame(smoothScroll);
      } else {
        isScrolling = false;
      }
    };

    const handleScroll = (event) => {
      event.preventDefault();
      targetScroll += event.deltaY;
      if (!isScrolling) {
        isScrolling = true;
        requestAnimationFrame(smoothScroll);
      }
    };

    window.addEventListener('wheel', handleScroll, { passive: false });
  }
}

// Usage example
document.addEventListener('DOMContentLoaded', () => {
  // Initialize ParallaxBackground with the desired element and parallax factor
  new ParallaxBackground('.gamble-background', -0.5);
  new ParallaxBackground('.background', -0.3); // Example with a different selector and parallax factor
});
