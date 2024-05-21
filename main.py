import sys
print(sys.path)

# Imported website package, and use the function create_app()
from website import create_app

app = create_app()

# this is to run the server on if condition is met, meaning main file is in the directory
if __name__ == '__main__':
    app.run(debug = True) # if we make any changes in the file, the server will automatically rerun, this is off False during production
    