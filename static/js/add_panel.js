"use strict";
let frm = document.forms.Item_2;
let building = frm.parent_building;
let parlor = frm.parent_parlor;
building.value = 'Корпус1'
//parlor.value = '1'
console.dir(building.value);
let a = 12;
console.log(parlor.value)
let b = Number(parlor.value);
let c = a/b;
console.log(c);