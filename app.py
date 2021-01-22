from flask import Flask, request, render_template
from inference import get_category, plot_category

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rock_paper_scissor():
    if request.method == 'POST':
    # POST Method to post the results file
        # Read file from upload
        img = request.files['file']
        # Get category of prediction
        image_category = get_category(img)
        # Plot the category
        plot_category(img)
        # Render the result template
        return render_template('result.html', category=image_category)
    # For GET requests, load the index file
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
