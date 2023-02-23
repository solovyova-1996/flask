from blog.app import crate_app

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
app = crate_app()
app.run(host='0.0.0.0', debug=True)