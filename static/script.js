""" var position = 0
var button = document.querySelector('#button')
var instruction = document.querySelector('#instruction')
button.addEventListener('click', function(){
position++
var text = exercises[position]
instruction.innerHTML = text
})
"""
