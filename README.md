
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
      background: linear-gradient(135deg, #d0e8ff, #f3fbff);
      color: #1f2937;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    header {
      background-color: #1e40af;
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
      color: #1e40af;
      margin-bottom: 1rem;
      text-align: center;
    }

    /* Trending Stories Section Styling */
    .trending {
      background: linear-gradient(120deg, #e0f2fe, #ffffff);
      padding: 2rem 1rem;
      border-radius: 16px;
      box-shadow: 0 8px 16px rgba(0,0,0,0.05);
      margin-bottom: 3rem;
    }
    .trending h2 {
      border-left: 5px solid #2563eb;
      padding-left: 10px;
      margin-bottom: 1.5rem;
      text-align: left;
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
      transition: box-shadow 0.3s ease;
    }

    .trending-card h3 {
      font-family: 'Roboto Slab', serif;
      color: #2563eb;
      margin-bottom: 10px;
      font-size: 1.1rem;
    }

    .trending-card p {
      font-size: 0.95rem;
      color: #374151;
      line-height: 1.4;
      overflow: hidden;
      max-height: 60px;
      transition: max-height 0.4s ease;
    }

    .trending-card p.expanded {
      max-height: 500px;
    }

    .trending-card button {
      margin-top: 10px;
      padding: 8px 14px;
      background-color: #2563eb;
      border: none;
      border-radius: 6px;
      color: white;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .trending-card button:hover {
      background-color: #1e40af;
    }

    .carousel-nav {
      margin-top: 1rem;
      text-align: center;
    }

    .carousel-nav button {
      margin: 0 8px;
      background-color: #2563eb;
      color: white;
      border: none;
      padding: 8px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
    }

    .carousel-nav button:hover {
      background-color: #1e40af;
    }

    /* News Grid Styling */
    .grid {
      background: linear-gradient(120deg, #f8fafc, #e2e8f0);
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
      color: #1f2937;
      font-family: 'Roboto Slab', serif;
      margin-bottom: 10px;
    }

    .content p {
      font-size: 0.95rem;
      color: #4b5563;
      line-height: 1.4;
      overflow: hidden;
      max-height: 60px;
      transition: max-height 0.4s ease;
    }

    .content p.expanded {
      max-height: 1000px;
    }

    .button {
      margin-top: 12px;
      padding: 10px 16px;
      background-color: #2563eb;
      color: white;
      border: none;
      border-radius: 6px;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.3s ease;
      align-self: flex-start;
    }

    .button:hover {
      background-color: #1e40af;
    }

    footer {
      background-color: #1e40af;
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
            <h3>Olica Felix Introduces innovations in Amolatar</h3>
            <p class="summary">Felix Olica a young innovative youth who hails from Akwon Subcounty in Amolatar district has started innovation by putting in place websites, online television and online radio. Through his Kyoga TV and Olix Radio which are broadcasting on www.kyogatv.com, Olica said he decided to come out with a new model, developed by a team of young youth that he took through trainings in his Olix Innobations Hub and Media Centre, preparing them to participate in radio and television broadcast, web development and hosting, digital marketing, media production among others.</p>
            <button class="toggle-summary">Read More</button>
          </article>
          <article class="trending-card">
            <h3>Economic Growth Hits Record High</h3>
            <p class="summary">The economy has surpassed expectations, with new job opportunities emerging worldwide. Recent fiscal strategies and trade agreements have contributed to this growth, with several sectors reporting double-digit improvements.</p>
            <button class="toggle-summary">Read More</button>
          </article>
          <article class="trending-card">
            <h3>Global Climate Initiatives</h3>
            <p class="summary">Countries unite to combat climate change with ambitious policies and green tech. A multi-nation summit produced a coordinated roadmap that includes zero-emission targets and major funding for climate research by 2030.</p>
            <button class="toggle-summary">Read More</button>
          </article>
        </div>
      </div>
      <div class="carousel-nav">
        <button onclick="changeSlide(-1)">Prev</button>
        <button onclick="changeSlide(1)">Next</button>
      </div>
    </section>

    <section class="grid" aria-label="Latest News Articles">
      <article class="card">
        <img src="https://northpointnews.net/wp-content/uploads/2023/07/quantum-ai.jpg" alt="Tech innovation" />
        <div class="content">
          <h2>Tech Innovation: What to Expect</h2>
          <p class="summary">Explore the newest trends shaping technology in 2025 and beyond. From quantum computing to AI-generated art, the boundaries of innovation are rapidly expanding.</p>
          <button class="toggle-summary button">Read More</button>
        </div>
      </article>
      <article class="card">
        <img src="https://northpointnews.net/wp-content/uploads/2023/07/finance-growth.jpg" alt="Economic updates" />
        <div class="content">
          <h2>Economic Updates</h2>
          <p class="summary">Markets react positively to recent policy changes designed to boost growth. Analysts point to an uptick in consumer confidence and business investment.</p>
          <button class="toggle-summary button">Read More</button>
        </div>
      </article>
      <article class="card">
        <img src="https://northpointnews.net/wp-content/uploads/2023/07/soccer-stadium.jpg" alt="Sports highlights" />
        <div class="content">
          <h2>Sports Highlights</h2>
          <p class="summary">Catch up on the latest games, scores, and player news from around the world. This season has brought excitement across all major leagues.</p>
          <button class="toggle-summary button">Read More</button>
        </div>
      </article>
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
    // Read More / Read Less toggle
    document.querySelectorAll('.toggle-summary').forEach(button => {
      button.addEventListener('click', () => {
        const card = button.closest('article');
        const summary = card.querySelector('.summary');
        const isExpanded = summary.classList.contains('expanded');

        summary.classList.toggle('expanded');
        button.textContent = isExpanded ? 'Read More' : 'Read Less';
      });
    });

    // Manual Trending Carousel
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
