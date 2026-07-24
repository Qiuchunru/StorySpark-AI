
from flask import Flask, render_template, request

app = Flask(__name__)


def generate_story(prompt, genre, tone):
    """
    Temporary AI response.
    Later replaced with IBM Granite API.
    """

    story = f"""
    Title:
    The Hidden World of {prompt}

    Genre:
    {genre}

    Tone:
    {tone}


    Summary:
    A creator discovers a mysterious world based on {prompt}.
    Through challenges and unexpected discoveries,
    the main character learns the true meaning of creativity.


    Characters:

    1. Alex
       A curious explorer searching for answers.

    2. Nova
       An AI companion helping create new possibilities.


    Ending:

    The journey inspires a new generation of creators.
    """

    return story



@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        prompt = request.form["prompt"]
        genre = request.form["genre"]
        tone = request.form["tone"]

        result = generate_story(
            prompt,
            genre,
            tone
        )


    return render_template(
        "index.html",
        result=result
    )



if __name__ == "__main__":
    app.run(debug=True)
