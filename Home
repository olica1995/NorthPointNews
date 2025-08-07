
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
      overflow-x: hidden;
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
      width: auto;
      height: auto;
      max-width: 100%;
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
      max-width: 100%;
    }

    .trending-carousel {
      display: flex;
      transition: transform 0.6s ease-in-out;
      width: 100%;
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
      word-wrap: break-word;
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
      min-height: 44px;
      min-width: 44px;
      font-size: 1rem;
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
      min-height: 44px;
      min-width: 44px;
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
      height: auto;
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
      min-height: 44px;
      min-width: 44px;
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

    /* Mobile tweaks */
    @media (max-width: 480px) {
      .trending-card,
      .card .content {
        padding: 16px 12px;
      }

      .carousel-nav button {
        padding: 6px 10px;
        font-size: 0.9rem;
      }

      .trending-card h3,
      .content h2 {
        font-size: 1rem;
      }

      .summary,
      .full-story {
        font-size: 0.9rem;
      }

      .grid {
        grid-template-columns: 1fr;
      }

      .logo-img {
        max-width: 100%;
        height: auto;
      }
    }
  </style>
</head>
<body>
  <header>
    <div style="display: flex; justify-content: center; align-items: center;">
      <img src="north point news logo.png" alt="North Point News Logo" class="logo-img" />
    </div>
  </header>

  <main>
    <!-- Trending Section -->
    <section class="trending" aria-label="Trending Stories">
      <h2>Trending Stories</h2>
      <div class="carousel-wrapper">
        <div class="trending-carousel" id="trendingCarousel">
          <!-- Slide 1 -->
          <article class="trending-card">
            <h3>Olica Felix Introduces Innovations in Amolatar</h3>
            <p class="summary">Felix Olica, a young innovative youth from Akwon Subcounty in Amolatar district, has begun creating online platforms...</p>
            <p class="full-story">Felix Olica, a young and innovative youth from Akwon Subcounty in Amolatar district, has started transforming the local media landscape. Through his entrepreneurial initiative, he has launched Kyoga TV and Olix Radio, both accessible at <a href="https://www.kyogatv.com" target="_blank">www.kyogatv.com</a>. These platforms aim to empower local voices, share regional stories, and provide a space for community dialogue.</p>
            <button class="toggle-summary">Read More</button>
          </article>

          <!-- Slide 2 -->
          <article class="trending-card">
            <h3>Economic Growth Hits Record High</h3>
            <p class="summary">The economy has surpassed expectations, with new job opportunities emerging worldwide...</p>
            <p class="full-story">Recent fiscal strategies and trade agreements have contributed to growth, with several sectors reporting double-digit improvements.</p>
            <button class="toggle-summary">Read More</button>
          </article>

          <!-- Slide 3 -->
          <article class="trending-card">
            <h3>Global Climate Initiatives</h3>
            <p class="summary">Countries unite to combat climate change with ambitious policies and green tech...</p>
            <p class="full-story">Countries around the world have united to combat climate change with ambitious environmental policies and investments in green technology.</p>
            <button class="toggle-summary">Read More</button>
          </article>
        </div>
      </div>
      <div class="carousel-nav">
        <button onclick="changeSlide(-1)">Prev</button>
        <button onclick="changeSlide(1)">Next</button>
      </div>
    </section>

    <!-- Latest News Grid -->
    <section class="latest-news" aria-label="Latest News">
      <h2>Latest News</h2>
      <div class="grid">
        <article class="card">
          <img src="https://images.unsplash.com/photo-1556740749-887f6717d7e4?auto=format&fit=crop&w=800&q=80" alt="Technology Update" />
          <div class="content">
            <h2>Breakthrough in Renewable Energy</h2>
            <p class="summary">Scientists develop new solar cells with higher efficiency and lower cost...</p>
            <p class="full-story">Next-gen solar cells increase energy conversion and lower production costs—potentially accelerating renewable energy adoption globally.</p>
            <button class="toggle-summary">Read More</button>
          </div>
        </article>

        <article class="card">
          <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80" alt="City Infrastructure" />
          <div class="content">
            <h2>Smart Cities Expansion</h2>
            <p class="summary">Urban areas embrace smart technology to improve services and reduce waste...</p>
            <p class="full-story">Cities worldwide are adopting smart technology to optimize resources, improve public safety, and enhance transportation networks.</p>
            <button class="toggle-summary">Read More</button>
          </div>
        </article>

        <article class="card">
          <img src="https://images.unsplash.com/photo-1495020689067-958852a7765e?auto=format&fit=crop&w=800&q=80" alt="Healthcare Innovation" />
          <div class="content">
            <h2>Healthcare Innovation Advances</h2>
            <p class="summary">New AI tools assist doctors in early disease detection and personalized treatments...</p>
            <p class="full-story">AI integration in healthcare is improving diagnosis, enabling early disease detection and personalized treatment plans.</p>
            <button class="toggle-summary">Read More</button>
          </div>
        </article>
      </div>
    </section>
  </main>

  <footer>
    <div class="footer-content">
      <div>© 2025 North Point News. All rights reserved.</div>
      <div class="footer-links">
        <a href="mailto:northpointnews92@gmail.com">📧 Email: northpointnews92@gmail.com</a>
        <a href="https://wa.me/256777626808" target="_blank" rel="noopener noreferrer">💬 WhatsApp: +256 777 626808</a>
      </div>
    </div>
  </footer>

  <script>
    document.querySelectorAll('.toggle-summary').forEach(button => {
      button.addEventListener('click', () => {
        const card = button.closest('article');
        const summary = card.querySelector('.summary');
        const full = card.querySelector('.full-story');
        const isExpanded = full.style.display === 'block';

        summary.style.display = isExpanded ? 'block' : 'none';
        full.style.display = isExpanded ? 'none' : 'block';
        button.textContent = isExpanded ? 'Read More' : 'Read Less';
      });
    });

    const carousel = document.getElementById('trendingCarousel');
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
