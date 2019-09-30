window.addEventListener("load",bindEvents);
function bindEvents(){
    document.querySelector('#add').addEventListener('click',addRecord);
}
let count = 0;
function addRecord(){
    var item = new Item();
    for(let key in item){
        item[key] = document.querySelector('#' + key).value;

    }
    count = count+1;
    itemOperations.add(item);
    printRecord(item);
}
function printRecord(item){
    var tbody = document.querySelector('#item');
    var tr = tbody.insertRow();
    var index = 0;
    for(let key in item){
        let cell = tr.insertCell(index);
        cell.innerText = item[key];
        index++;
    }
}