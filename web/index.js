const fetchData = (filter) => {
    return new Promise((resolve, reject) => {
        fetch(`http://localhost:3000/app?ten=${filter}`)
            .then(function (response) {
                console.log('response:', response.data);
                data = response;
                return resolve(data);
            })
            .catch(function (error) {
                return reject(error)
            });
    })
}
let filter = ''
fetchData(filter).then(result => {
    data = result;
    console.log('data:', data);
})