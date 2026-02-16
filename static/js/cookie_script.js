
window.addEventListener("load", function(){
    window.cookieconsent.initialise({
        palette: {
            popup: { background: "#000" },
            button: { background: "#f1d600" }
        },
        theme: "classic",
        content: {
            message: "We use cookies to enhance your experience.",
            dismiss: "Got it!",
            link: "Learn more",
            href: "{% url 'privacy_policy' %}"
        }
    });
});

