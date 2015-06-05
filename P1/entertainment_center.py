import media
import fresh_tomatoes

gramm = media.Movie(
            title="1001 Gramm",
            trailer_youtube_url="https://www.youtube.com/watch?v=FVIAtIHcehM",
            poster_image_url="http://goo.gl/q6y0Q3")

chocolat = media.Movie(
            title="Chocolat",
            trailer_youtube_url="https://www.youtube.com/watch?v=zH3dNtJGcn8",
            poster_image_url="http://goo.gl/59Xcv8")

# creates HTML of movies page and opens it in a browser
fresh_tomatoes.open_movies_page([gramm, chocolat])
