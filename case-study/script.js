const ctx=document.getElementById("authChart");

new Chart(ctx,{
type:"bar",
data:{
labels:["OAuth2","API Key","Bearer","Basic","Unknown"],
datasets:[{
label:"Apps",
data:[52,28,11,4,5]
}]
},
options:{
responsive:true,
plugins:{
legend:{
labels:{color:"white"}
}
},
scales:{
x:{
ticks:{color:"white"},
grid:{color:"#334155"}
},
y:{
ticks:{color:"white"},
grid:{color:"#334155"}
}
}
}
});