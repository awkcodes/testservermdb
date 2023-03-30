fetch(`http://localhost:8000/api/registration/accounts/profile`, {
        method: 'GET',
        headers: { "Authorization": "Token c88d3dba2643fdca6b783c2486d6c68371e274f9" }
    })
        .then(response => response.json())
