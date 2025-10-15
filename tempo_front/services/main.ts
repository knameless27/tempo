import {ofetch} from "ofetch"

const tFetch = ofetch.create({
    baseURL: 'http://localhost/api',
    onRequest({request, options}) {
        console.log(request)
    },
    onRequestError(error) {
        console.log(error)
    },
    onResponse({request, options}) {
        console.log(request)
    },
    onResponseError(error) {
        console.log(error)
    },
})

export default tFetch