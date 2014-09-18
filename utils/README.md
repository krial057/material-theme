Utils
================

I wrote the css in stylus.
because the css contains data-bindings, stylus throws errors.
To fix this, I wrote a little python script that enables data-bindings for the colors in the stylus file. 
You can use _primaryColor500_ and _accentColor200_ inside the stylus file to refer to the bound colors. (you can replace 500 with any numeber you want that is shown in the spec)

After runnging the python script, you have to manually copy the content of the created file into the material-theme element.