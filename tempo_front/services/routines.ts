import tFetch from "./main";

const getRoutines = await tFetch('routines', {
    method: "GET"
})