$(document).ready(function(){
	
	var l = new ol.layer.Tile({
		source: new ol.source.TileWMS({
			url:'http://localhost:8090/geoserver/wms',
			params: {LAYERS: 'PythonAlergies:patiente_postgis', VRESION: '1.1.1'}
		})
	});

	var l1 = new ol.layer.Tile({
		opacity:0.5,
		source: new ol.source.TileWMS({
			url:'http://localhost:8090/geoserver/wms',
			params: {LAYERS: 'PythonAlergies:SRB_adm1', VRESION: '1.1.1'}
		}),
		style: new ol.style.Style({
			fill: new ol.style.Fill({
				color:'blue'
			}),
			stroke: new ol.style.Stroke({
				color:'red',
				width:0.99
			})
		})
	});

	var osm = new ol.layer.Tile({
		  source: new ol.source.OSM()
	});

	  var map = new ol.Map({
	    target: 'map',
	    layers: [
	     	osm, l1,l		
	      
	    ],
	    view: new ol.View({
	      projection: 'EPSG:4326',
	      center: [20.8, 44.5],
	      zoom: 7,
	      maxResolution: 0.703125
	    })
	  });
	  
	map.on('click',function(){
	{% if request.user.is_authenticated %}
		
		alert("You are logged in, you can proceed to your dashboard");
	{% else %}
		
		alert("You must be registred to see data");
	{% endif %}
	});
	  
	/* Image Slider*/ 
	var mainImage = $('#mainImage > img');
	var sources = [
					'{% static "images/alVscold.jpg" %}',
					'{% static "images/child.jpg" %}',
					'{% static "images/dina.jpg" %}',
					'{% static "images/gw.jpg" %}',
					'{% static "images/Pollen.jpg" %}',
					'{% static "images/rec1.jpg" %}',
					'{% static "images/rec2.jpg" %}',
					'{% static "images/rec4.jpeg" %}',
					'{% static "images/rec5.jpeg" %}',
					'{% static "images/rec6.jpg" %}',
					'{% static "images/rec7.jpeg" %}',
					'{% static "images/rec8.jpeg" %}'
				]
					
	function getRandomIntInclusive(min, max) {
		min = Math.ceil(min);
		max = Math.floor(max);
		return Math.floor(Math.random() * (max - min + 1)) + min;
	}
	function changeImage(){
		var num = getRandomIntInclusive(0,sources.length - 1);
		var src = sources[num]; 
		mainImage.fadeOut(2500,function(){
			$(this).attr('src',src);
		}).fadeIn(2000);
		
	}

	setInterval(changeImage,5000);



	
	
	
});



