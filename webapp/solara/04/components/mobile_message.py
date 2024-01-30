import solara as sol

html_media = """
<head>
<style>
    @media only screen and (max-width: 600px) {
        .mobile-only {
            display: block;
        }
    }

    @media only screen and (min-width: 601px) {
        .mobile-only {
            display: none;
        }
    }
    p {
        background-color: #f1f1f1;
    }
</style>
</head>

<p class="mobile-only">
    Swipe right to see content
</p>
"""

css = """
    .trial-html {
        background-color: red;
        }
"""

@sol.component
def mobile_message():
    with sol.VBox() as main:
        sol.Style(css)
        sol.HTML(unsafe_innerHTML=html_media, classes=["trial-html"])
    return main
