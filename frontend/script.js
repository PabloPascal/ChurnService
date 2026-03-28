document.getElementById('churnForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');
    const predictBtn = document.getElementById('predictBtn');
    const btnText = predictBtn.querySelector('span');
    const spinner = predictBtn.querySelector('.spinner');

    // UI состояния
    resultDiv.classList.add('hidden');
    errorDiv.classList.add('hidden');
    btnText.textContent = 'Predicting...';
    spinner.classList.remove('hidden');
    predictBtn.disabled = true;

    const formData = {
        CreditScore: parseInt(document.getElementById('CreditScore').value),
        Age: parseInt(document.getElementById('Age').value),
        Tenure: parseInt(document.getElementById('Tenure').value),
        Balance: parseFloat(document.getElementById('Balance').value),
        NumOfProducts: parseInt(document.getElementById('NumOfProducts').value),
        HasCrCard: parseInt(document.getElementById('HasCrCard').value),
        IsActiveMember: parseInt(document.getElementById('IsActiveMember').value),
        EstimatedSalary: parseFloat(document.getElementById('EstimatedSalary').value),
        Geography: document.getElementById('Geography').value,
        Gender: document.getElementById('Gender').value
    };

    try {
        const response = await fetch('http://localhost:8080/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            let errorMsg = `HTTP ${response.status}`;
            try {
                const errData = await response.json();
                errorMsg = errData.detail || errorMsg;
            } catch {}
            throw new Error(errorMsg);
        }

        const data = await response.json();
        const probabilityPercent = (data.churn_probability * 100).toFixed(1);
        const willChurn = data.churn_prediction === 1 ? 'Yes' : 'No';

        document.getElementById('probability').textContent = probabilityPercent;
        document.getElementById('prediction').textContent = willChurn;

        resultDiv.classList.remove('hidden');
    } catch (err) {
        errorDiv.textContent = `❌ ${err.message}`;
        errorDiv.classList.remove('hidden');
    } finally {
        btnText.textContent = 'Predict Churn';
        spinner.classList.add('hidden');
        predictBtn.disabled = false;
    }
});