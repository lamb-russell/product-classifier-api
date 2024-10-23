document.getElementById('submitBtn').addEventListener('click', async () => {
    // Get the input values
    const description = document.getElementById('description').value;
    const categories = document.getElementById('categories').value.split(',');
    const model_name = document.getElementById('model_name').value;

    // Prepare the payload
    const payload = {
        description: description,
        categories: categories,
        model_name: model_name
    };

    try {
        // Log the payload to see if it's correct
        console.log("Sending payload:", payload);

        // Make the API call using fetch
        const response = await fetch('http://127.0.0.1:8000/classify', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload)
        });

        // Check if the response is OK
        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }

        // Parse the JSON response
        const data = await response.json();

        // Log and display the response
        console.log("Response from API:", data);
        document.getElementById('apiResponse').textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        // Log and display any errors
        console.error('API call failed:', error);
        document.getElementById('apiResponse').textContent = 'Error: ' + error.message;
    }
});
