function changeClass(elm){
	if(document.getElementById(elm).getAttribute('class')=='bi bi-x'){
		document.getElementById(elm).setAttribute('class','bi bi-list');
		document.getElementsByClassName('navbar-toggler').style.backgroundColor='#085394 !important';
	}else{
		document.getElementById(elm).setAttribute('class','bi bi-x');
		document.getElementsByClassName('navbar-toggler').style.backgroundColor='#0d0 !important';
	}
}