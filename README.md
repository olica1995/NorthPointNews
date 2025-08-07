<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>North Point News</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Roboto+Slab&display=swap" rel="stylesheet" />
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: 'Inter', sans-serif;
      background: linear-gradient(135deg, #d9fdd3, #f0fff4);
      color: #1f2937;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      background-color: #000;
      color: white;
      padding: 1rem 2rem;
      text-align: center;
      box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }

    .logo-img {
      max-height: 60px;
      user-select: none;
    }

    main {
      flex: 1;
      max-width: 1200px;
      margin: 2rem auto;
      padding: 0 1rem;
      width: 100%;
    }

    h1, h2 {
      font-family: 'Roboto Slab', serif;
      color: #000;
      margin-bottom: 1rem;
      text-align: center;
    }

    .trending {
      background: red;
      padding: 2rem 1rem;
      border-radius: 16px;
      box-shadow: 0 8px 16px rgba(0,0,0,0.05);
      margin-bottom: 3rem;
    }

    .trending h2 {
      border-left: 5px solid black;
      padding-left: 10px;
      margin-bottom: 1.5rem;
      text-align: left;
      color: #fff;
    }

    .carousel-wrapper {
      position: relative;
      overflow: hidden;
    }

    .trending-carousel {
      display: flex;
      transition: transform 0.6s ease-in-out;
    }

    .trending-card {
      flex: 0 0 100%;
      max-width: 100%;
      background-color: #ffffffd9;
      backdrop-filter: blur(6px);
      padding: 20px;
      border-radius: 16px;
      box-shadow: 0 10px 20px rgba(0, 0, 0, 0.07);
    }

    .trending-card h3 {
      font-family: 'Roboto Slab', serif;
      color: black;
      margin-bottom: 10px;
      font-size: 1.1rem;
    }

    .summary,
    .full-story {
      font-size: 0.95rem;
      color: #374151;
      line-height: 1.4;
    }

    .full-story {
      display: none;
    }

    .trending-card button {
      margin-top: 10px;
      padding: 8px 14px;
      background-color: black;
      border: none;
      border-radius: 6px;
      color: white;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .trending-card button:hover {
      background-color: #333;
    }

    .carousel-nav {
      margin-top: 1rem;
      text-align: center;
    }

    .carousel-nav button {
      margin: 0 8px;
      background-color: black;
      color: white;
      border: none;
      padding: 8px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
    }

    .carousel-nav button:hover {
      background-color: #333;
    }

    .grid {
      background: linear-gradient(120deg, #f0fff4, #d9fdd3);
      padding: 2rem 1rem;
      border-radius: 16px;
      box-shadow: 0 8px 16px rgba(0,0,0,0.05);
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 24px;
    }

    .card {
      background: white;
      border-radius: 16px;
      box-shadow: 0 10px 20px rgba(0,0,0,0.1);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.3s, box-shadow 0.3s;
    }

    .card:hover {
      transform: scale(1.03);
      box-shadow: 0 20px 30px rgba(0,0,0,0.15);
    }

    .card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
      user-select: none;
    }

    .content {
      padding: 16px;
      display: flex;
      flex-direction: column;
    }

    .content h2 {
      font-size: 1.2rem;
      color: black;
      font-family: 'Roboto Slab', serif;
      margin-bottom: 10px;
    }

    .button {
      margin-top: 12px;
      padding: 10px 16px;
      background-color: black;
      color: white;
      border: none;
      border-radius: 6px;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.3s ease;
      align-self: flex-start;
    }

    .button:hover {
      background-color: #333;
    }

    .latest-news h2 {
      font-family: 'Roboto Slab', serif;
      color: #000;
      margin-bottom: 1.5rem;
      text-align: center;
    }

    footer {
      background-color: #000;
      color: white;
      padding: 1.5rem 1rem;
      text-align: center;
      font-family: 'Roboto Slab', serif;
    }

    .footer-content {
      max-width: 1000px;
      margin: 0 auto;
    }

    .footer-links {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 1rem;
      margin-top: 0.8rem;
    }

    .footer-links a {
      color: #93c5fd;
      text-decoration: none;
      font-weight: 500;
    }

    .footer-links a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <header>
    <img src="north point news logo.png" alt="North Point News Logo" class="logo-img" />
  </header>

  <main>
    <section class="trending" aria-label="Trending Stories">
      <h2>Trending Stories</h2>
      <div class="carousel-wrapper">
        <div class="trending-carousel" id="trendingCarousel">
          <article class="trending-card">
            <h3>Olica Felix Introduces Innovations in Amolatar</h3>
            <p class="summary">Felix Olica, a young innovative youth from Akwon Subcounty in Amolatar district, has begun creating online platforms...</p>
            <p class="full-story">Felix Olica, a young and innovative youth from Akwon Subcounty in Amolatar district, has started transforming the local media landscape. Through his entrepreneurial initiative, he has launched Kyoga TV and Olix Radio, both accessible at <a href="https://www.kyogatv.com" target="_blank">www.kyogatv.com</a>. These platforms aim to empower local voices, share regional stories, and provide a space for community dialogue. Olica says his vision is to inspire young people to use technology creatively to address social challenges and bring development to rural communities.</p>
            <button class="toggle-summary">Read More</button>
          </article>

          <article class="trending-card">
            <h3>Economic Growth Hits Record High</h3>
            <p class="summary">The economy has surpassed expectations, with new job opportunities emerging worldwide...</p>
            <p class="full-story">The economy has surpassed expectations, with new job opportunities emerging worldwide. Recent fiscal strategies and trade agreements have contributed to this growth, with several sectors reporting double-digit improvements. Economists are optimistic that sustained investment will continue to drive expansion in emerging markets and beyond.</p>
            <button class="toggle-summary">Read More</button>
          </article>

          <article class="trending-card">
            <h3>Global Climate Initiatives</h3>
            <p class="summary">Countries unite to combat climate change with ambitious policies and green tech...</p>
carousel = document.getElementById('trendingCarousel');
    const trendingCards = carousel.querySelectorAll('.trending-card');
    let currentIndex = 0;

    function changeSlide(direction) {
      currentIndex += direction;
      if (currentIndex < 0) currentIndex = trendingCards.length - 1;
      if (currentIndex >= trendingCards.length) currentIndex = 0;
      carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
    }
  </script>
</body>
</html>
