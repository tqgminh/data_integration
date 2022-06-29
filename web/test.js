import axios from 'axios';

let filter = 'iPhone';
let data;
const fetchData = async (filter) => {
    await axios.get(`http://localhost:3000/app?ten=${filter}`)
    .then(function (response) {
        data = response.data.data;
    })
    .catch(function (error) {
        console.log(error);
    })
    console.log(data);
}
fetchData(filter)
console.log('data:', data);