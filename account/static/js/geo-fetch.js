const countryDropdown = document.getElementById('id_country');
const regionDropdown = document.getElementById('id_region');

countryDropdown.addEventListener('change', (event) => {
    const selectedCountry = event.target.value;
    if (selectedCountry) {

        fetch(`http://127.0.0.1:8000/api/regions/?country=${selectedCountry}`, { mode: "same-origin" })
            .then(response => response.json())
            .then(regions => {
                // Clear existing options
                regionDropdown.innerHTML = '<option value="">Region</option>';
                // Add new options
                regions.forEach(region => {
                    const option = document.createElement('option');
                    option.value = region.id;
                    option.text = region.title;
                    regionDropdown.add(option);
                });
            })
            .catch(error => console.error(error));
    } else {
        // Clear city dropdown if no country is selected
        regionDropdown.innerHTML = '<option value="">Region</option>';
    }
});