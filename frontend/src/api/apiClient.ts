import axios from "axios"

const apiClient = axios.create({
    baseURL: "http://localhost:8000/api/v1",
    timeout: 5000
})

export default apiClient;