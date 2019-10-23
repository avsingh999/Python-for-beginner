<h1> Learn Django </h1>

<h2> What is Django? </h2>

<p> Django is a Python-based free and open-source web framework that encourages rapid development and clean, pragmatic design.
Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app
without needing to reinvent the wheel.   </p>

<p> Django has one very simple principle – Don’t Repeat Yourself. The principle is all about keeping the code non-repeating and
simple which makes it more readable. </p>

<h2> Why choose Django? </h2>
Some of the reason to choose Django are:
<ul>
  <li> <strong> Ridiculously fast: </strong> <br>  Django was designed to help developers take applications from concept to
  completion as quickly as possible. </li>
  <li>  <strong> Reassuringly secure: </strong> <br> Django takes security seriously and helps developers avoid many common
  security mistakes.   </li>
  <li>  <strong> Exceedingly scalable: </strong> <br> Some of the busiest sites on the Web leverage Django’s ability to quickly
  and flexibly scale   </li>
</ul>

<h2> Django Installation </h2>

<p>  Django being Python web framework requires Python. To install Python on your system, go to <a href="https://www.python.org/downloads/">
https://www.python.org/downloads/</a>. After installation run the following command to check if python is properly installed in your system:
</p>

<code>$ python --version </code>

<p>We will use pip to install django. If your distribution doesnot have pip installed, you can install it from 
<a href="https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py">here.</a> </p>
<p> You can use <a href="https://virtualenv.pypa.io/">virtualenv</a> to create isolated Python environments,
which are more practical than installing packages systemwide. </p>
<p>Now you can run following command to install django </p>
<code>$ pip install Django</code>

<h2>Building your first Web Application</h2>

<p>Now let's create a simple Hello World Web application using django.</p>
<p>The first thing we need to do is create a project. Go to the directory you want to create your project and enter the following command:</p>
<code> $ django-admin startproject hello_world</code> <br>

<p>Your project is now created. You can see new directories created, let's see what it does:</p>

<ul>
	<li><strong>manage.py : </strong>It is a command-line utility that lets you interact with this Django project in various ways. </li>
	<li><strong>urls.py : </strong>The URL declarations for this Django project; a “table of contents” of your Django-powered site. </li>
	<li><strong>settings.py : </strong>Settings/configuration for this Django project.</li>
	<li><strong>__init__.py : </strong> An empty file that tells Python that this directory should be considered a Python packag</li>
	<li><strong>wsgi.py :</strong>An entry-point for WSGI-compatible web servers to serve your project</li>
	<li><strong>hello_world : </strong>This  is the actual Python package for your project. Its name is the Python package name you’ll 
  need to use to import anything inside it</li>
</ul>

<p>Now to create your application make sure you are in the same directory as <code>manage.py</code> and enter the following command:</p>
<code>python manage.py startapp hello</code>

<p>Now a new directory 'hello' is created which includes views, model, test and so on. Now the next thing you need to do is import your 
app inside project settings. Open hello_world/settings.py and under <code>INSTALLED_APPS</code> add <code> 'hello',</code></p>
<pre><code>
	...
	
	INSTALLED_APPS = [
    	'django.contrib.admin',
    	'django.contrib.auth',
    	'django.contrib.contenttypes',
    	'django.contrib.sessions',
    	'django.contrib.messages',
    	'django.contrib.staticfiles',

    	'hello'
	]

</code></pre>

<p>Now let's create a view. Open hello/views.py and following code:</p>
<pre><code>from django.shortcuts import render
def index(request):
	return render(request, 'hello/index.html')</code> </pre>
 
<p>We have created a view, now let's add templates it can render. Go to your app directory and create a 
folder named <code>templates</code>. Inside the templates directory create a new folder named <code>hello</code>.
Finally inside hello directory create a file 'index.html' </p>
<p>The path will be something like this:</p>
<pre><code>hello/templates/hello/index.html</code></pre>
ie
<pre><code>app_name/templates/app_name/files.html</code></pre>

<br>
<p>Now in 'index.html' add the following: </p><br>
<pre><code>Hello World!!</code></pre>

  <p>Now we need to map our view to URL. So let's create a new 'urls.py' file inside our 'hello' app. in 'hello/urls.py' add
  the following code: </p>
<pre><code>
    from django.urls import path
    from .views import index

      urlpatterns = [
        path('', index, name='index'),
      ]
</code></pre>
<br>
<p>The above code will return 'index' view from views.py </p>
<p>In the next step we make changes to the root 'urls.py' file. Open 'hello_world/urls.py' file and write following codes: </p>

<pre><code>
	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', include('hello.urls')),
	]
</code></pre>
<p>The include() function allows referencing other URLconfs. Whenever Django encounters include(),
it chops off whatever part of the URL matched up to that point and sends
the remaining string to the included URLconf for further processing.</p>

<p>We have now created a basic web app. To see what we have created we need to start the server. Go to the
same directory as 'manage.py' and enter the following command: </p>
<pre><code>python manage.py runserver</code></pre>
<br>
<p>After running the server navigate to <a href="http://localhost:8000/">http://localhost:8000/</a>.You will see 
'Hello World!' displayed on screen. The same hello world we defined in our 'index.html' file.</p>
<p> You can find the source sode of the app we just created <a href="https://github.com/beingbiplov/Python-for-beginner/tree/learnDjango/Learn%20Django/hello_world">Here</a> </p>

<p><strong>CONGRATULATIONS</strong>, you have created a basic functioning django web app.</p>

<h2>Learning Materials: </h2>
<ul>
	<li><h3><a href="https://docs.djangoproject.com/en/2.2/">
Django documentation : </a></h3> 
	Everything you need to know about Django.
 </li>
 <li>
	<h3><a href="https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/">A Complete Beginner's Guide to Django : </a></h3>
	A complete beginner’s guide to start learning Django.
</li>

 <li><h3><a href="https://docs.djangoproject.com/en/2.2/intro/tutorial01/">Create a basic poll application: </a></h3>
 	Tutorial that will walk you through the creation of a basic poll application.
 </li>
 <li>
	<h3><a href="https://tutorial.djangogirls.org/en/">Django Girls Tutorial : </a></h3>
	Build a blog app using function based views.
</li>


<li>
	<h3><a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django">
		Mozilla Django Tutorial: 
	</a></h3> Create a library application.
</li>

</ul>
