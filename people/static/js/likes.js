document.getElementById("template-styles").remove()
const csrftoken = Cookies.get('csrftoken')
const likeButton = document.getElementById("like-btn")
const likeNumber = document.getElementById("likes-btn-num")
const profileId = JSON.stringify({ profile_id: profile_id })
likeButton.addEventListener("click", event => {
    fetch("http://127.0.0.1:8000/api/like/", {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        mode: "same-origin",
        body: profileId
    })
        .then(response => response.json())
        .then(like => {
            if (like["is_liked"]) {
                likeNumber.innerHTML++
                likeButton.style.color = "#fc033d"
            }
            else {
                likeNumber.innerHTML--
                likeButton.style.color = ""
            }
        }
        )
        .catch(error => console.error(error))
})