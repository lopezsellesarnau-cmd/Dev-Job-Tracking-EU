STEPS
1_ Get the API from Adzuna and storit on Notes for the moment. (in the future in the .env).
1.1_ Create a repo on GitHub. (done(Dev-Job-Tracking-EU))
1.2_ Create fetch.py
2_ Start with the backend with Python, importing the fast API and Pandas.
3_ Once i see the code save the API on save environment (.env) (done)
4_ See the data on the terminal or elsewhere.
5_ Start with the HTML file for the front end
6_ Create the CSS file to apply the style (minimal, clear, white, thin lines, smooth lecture.)
7_ Connect with the JS file script.js to connect the frontand and backend.
8_ Create a 2D map for the countries, the one that more jobs available for juniors is bigger than the others, from bigger to smaller. (related with the data).
9_ Next step is to filter the senior by role and country. (% senior = count("senior frontend") / count("frontend") × 100)

DESICIONS
1_ Use SQLite because is an embeded, serverless database engine that reads and writes in one single file, instead of PostgreSQL, because v1 doesn't need a server, and I can move later if it grows.
2_ Use python for the backend, because is one the main programing languages and very versatile, and fast do develp a backend or prototype, and is the programming languages that i'm learing in the Python Helsiny Porgramming cours.
3_ Use pandas to manipulate the data or clean data that recives from the Adzuna API.
4_ HTML because is absolute important for every web site and I can build the skelethon of the web and i wanted to learn the fundamentals plus in this version it doesn't need a framework.
5_ CSS because it controles the visual presentation and is where i can apply the style that i want to my website.
6_ JavaScript because is the one that runes inside a web browser, and I can connect the front-end and back-end with a script.js file.
7_ Minimal and Editorial UI is because when the data, graphs, outcomes is presented with a clear, open space between blocks the user can feel is not overwhelmed, and finds the data in less time. It aslo the syle I most atractive find for a project and combine it with an editorial subtitles and lines we can create true clean art.
8_ Adzuna becouse is where we can get actual data from the selected countries and we can get an API from Adzuna to conect that data into our project.
9_FastAPI because python framwork and and I can build a robust and efficent API and is one of the fasted framworks in python and offering performance benchmarks comparable to Node.js
10_ Fetch.py because it collects the data from the Adzuna.
11_ Based on the first version on the project i've seen that some roles like "Product Engineer" or "Design Engineer has way more roles opened than frontend or backend because those roles also incloude mechanical or not dev roles, and the overall data is not saying if they are senior or junior, in this case we are looking for "junior" roles. 
12_ I've used the variable show_title to take a closer look at "product engineer" in DE(Germany) I have concluded that many of those roles are with a hardware focus not software which is the porpuse of the project, so I have decided to exclude "product engineer" for this version. The same applys to "Design Engineer" since most of the titles are: "electromechanics", "nanotech", "warfare".
13_ Testing different roles I have seen that most of the roles are not junior but senior or doesn't specify the role level. I have decided to keep the senior and junior together and look the actual trend of the market.
14_ Based on printing the titles from diferent roles, I have seen that in DE(Germany), many of the jobs are senior with the exception of full stack and more or less UX/UI.
15_ After testing the previous roles (Fronend, Backend, Full Stack & UX) I have seen the need of ad new roles that i didn't inclouded on the v1, I have added Web developer, software developer and mobile developer. After seeing the data tested in the regions DE and NL, I have concluded that the more specific it is like pure fronend and pure backend more senior roles are, and the more generics like full stack, web dev, or software dev have more "junior" & eng job postings. 