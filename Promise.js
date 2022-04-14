"use strict";
const myPromise =    fetch('https://api.github.com/users')
;
myPromise.then(function(response){
    response.json().then(function(users){
        users.forEach(function(user){
        console.log(user.login76)
    })})});

console.log(myPromise)
myPromise.then(response => console.log(response));

myPromise.catch(error => console.error(error));

console.log(myPromise);
console.log("Hello")


fetch("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a").then(function(response){
    console.log(response);
}).catch(function(error){
    console.log(error)
})

fetch("").then(function(response){
    response.json().then(function(users){
        users.forEach(function(user){
            console.log(user);
        })
    })
})