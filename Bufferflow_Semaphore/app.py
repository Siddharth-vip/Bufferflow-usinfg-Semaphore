from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML page

@app.route('/action/<operation>')
def action(operation):
    if operation == 'load':
        return load_goods()
    elif operation == 'unload':
        return unload_goods()
    elif operation == 'import':
        return import_goods()
    elif operation == 'export':
        return export_goods()
    elif operation == 'quit':
        return f"System quitting... Import queue: {import_queue.qsize()}, Export queue: {export_queue.qsize()}"
    else:
        return "Invalid operation!"

# Example placeholder functions (replace these with the full implementation)
def load_goods():
    return "Loaded goods."

def unload_goods():
    return "Unloaded goods."

def import_goods():
    return "Imported goods."

def export_goods():
    return "Exported goods."

if __name__ == '__main__':
    app.run(debug=True)
