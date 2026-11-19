
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("complaintForm");
    const textarea = document.getElementById("complaintText");

    const count = document.getElementById("characterCount");
    const clearButton = document.getElementById("clearButton");
    const predictButton = document.getElementById("predictButton");

    const loading = document.getElementById("loadingMessage");
    const error = document.getElementById("errorMessage");

    const emptyResult = document.getElementById("emptyResult");
    const predictionResult = document.getElementById("predictionResult");

    const category = document.getElementById("predictedCategory");
    const processedText = document.getElementById("processedText");

    // =====================================
    // CLASSIFICATION FUNCTIONALITY
    // =====================================

    if (!form || !textarea) return;

    // Reset result area to initial state
    function showAwaitingState() {

        loading.hidden = true;
        predictionResult.hidden = true;
        emptyResult.hidden = false;
        error.hidden = true;
        error.textContent = "";

    }

    // Character counter and clear previous result on editing
    textarea.addEventListener("input", function () {

        count.textContent = `${textarea.value.length} characters`;

        showAwaitingState();

    });

    // Clear button
    clearButton.addEventListener("click", function () {

        textarea.value = "";

        count.textContent = "0 characters";

        showAwaitingState();

        textarea.focus();

    });

    // Submit complaint
    form.addEventListener("submit", async function (event) {

        event.preventDefault();

        const complaint = textarea.value.trim();

        // Validate empty input
        if (!complaint) {

            loading.hidden = true;
            predictionResult.hidden = true;
            emptyResult.hidden = false;

            error.textContent =
                "Please enter a complaint before submitting.";

            error.hidden = false;

            return;
        }

        // Start loading state
        error.hidden = true;
        error.textContent = "";

        emptyResult.hidden = true;
        predictionResult.hidden = true;
        loading.hidden = false;

        predictButton.disabled = true;

        try {

            const response = await fetch("/predict", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    complaint: complaint
                })

            });

            const result = await response.json();

            if (!response.ok || !result.success) {

                throw new Error(
                    result.error || "Unable to classify complaint."
                );

            }

            // Display prediction
            category.textContent =
                result.predicted_category || "Category unavailable";

            processedText.textContent =
                result.processed_text || "No processed text returned.";

            predictionResult.hidden = false;
            emptyResult.hidden = true;

        }

        catch (err) {

            error.textContent =
                err.message || "Something went wrong. Please try again.";

            error.hidden = false;

            predictionResult.hidden = true;
            emptyResult.hidden = false;

        }

        finally {

            loading.hidden = true;

            predictButton.disabled = false;

            if (window.lucide) {
                lucide.createIcons();
            }

        }

    });

});
