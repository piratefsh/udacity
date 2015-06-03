import media
import fresh_tomatoes

gramm = media.Movie(title="1001 Gramm", 
	trailer_youtube_url="https://www.youtube.com/watch?v=FVIAtIHcehM",
	poster_image_url="http://t2.gstatic.com/images?q=tbn:ANd9GcQuEzifstiKe2hcfhlG9XrOY8gwgYLi0bydQyfifNT4btRqoAj4")

chocolat = media.Movie(title="Chocolat", 
	trailer_youtube_url="https://www.youtube.com/watch?v=zH3dNtJGcn8",
	poster_image_url="http://t2.gstatic.com/images?q=tbn:ANd9GcSAA-9RVzQYsZFzKRsGrOnQnrK1OuNf3GFPstf_JpIvvn2Zrtks")

fresh_tomatoes.open_movies_page([gramm, chocolat])