$(document).ready(function(){
	
	
	var style = new ol.style.Style({
		fill: new ol.style.Fill({
			color: 'blue'
		}),
		stroke: new ol.style.Stroke({
			color:'red'
		})
	});
/*######################################################################################################*/
/************************************Layer Definitions***************************************************/

// WMS With Serbian Borders 
var Borders_WMS = new ol.layer.Tile({
	title: "Borders",
	opacity:0.4,
	source: new ol.source.TileWMS({
		url: 'http://localhost:8090/geoserver/wms',
		params: {LAYERS: 'PythonAlergies:SRB_adm1', VERSION: '1.1.1'}
	})
});

// WMS With Patientes Data 
var Patientes_WMS = new ol.layer.Tile({
	title: "Patientes",
	source: new ol.source.TileWMS({
		url: 'http://localhost:8090/geoserver/wms',
		params: {LAYERS: 'PythonAlergies:patiente_postgis', VERSION: '1.1.1'}
	})
});

// Style For WFS Layer Serbian Borders -->
var styleRegionBorders = new ol.style.Style({
	fill: new ol.style.Fill({
		color: 'green'
	}),
	stroke: new ol.style.Stroke({
		color: 'brown',
		width: 3
	})
	
});


/*var chb = $('input[type=checkbox]');
alert(chb.length);
for(var i in chb){
	console.log(i+":"+chb[i]);
}
alert(chb.attr('type'));



chb.on('click',function(){
	var idName = $(this).attr('id');
	alert(idName);
});*/

// Styling Patientes With Function -->
var style_Patientes = (function(){
	var woman = [new ol.style.Style({
		image: new ol.style.Circle({
			fill: new ol.style.Fill({ color: 'red'}),
			radius: 10
		}),
		
	})];
		
	var man = [new ol.style.Style({
		image: new ol.style.Circle({
			fill: new ol.style.Fill({ color: 'blue'}),
			radius: 10
		})
	})];
		
	return function(feature, resolution){
		if(feature.get('pol') == "Z"){
			return woman;
		}else {
			return man;
		}
	};
})();
// WFS Layer For Borders -->
var WFS_Borders = new ol.layer.Vector({
	title: "Borders WFS",
	name: 'WFS_Borders',
	opacity: 0.45,
	source: new ol.source.Vector({
		loader: function(extent){
			$.ajax("http://localhost:8090/geoserver/wfs",{
				type: "GET",
				data: {
					service: "WFS",
					version: "1.1.0",
					request: "GetFeature",
					typename: "PythonAlergies:SRB_adm1",
					srsname: "EPSG:4326",
					outputFormat: "application/json",
					bbox: extent.join(",")+',EPSG:4326'
				}
			}).done(function(response,status){
				
				WFS_Borders.getSource().addFeatures(new ol.format.GeoJSON().readFeatures(response));
			})
		},
		strategy: ol.loadingstrategy.bbox,
		projection: 'EPSG:4326'
	}),
	style: styleRegionBorders
});	

// WFS Layer For Patientes -->
var WFS_Patientes = new ol.layer.Vector({
	title: "Patientes WFS",
	name: 'WFS_Patientes',
	opacity: 0.8,
	source: new ol.source.Vector({
		loader: function(extent){
			$.ajax("http://localhost:8090/geoserver/wfs",{
				type: "GET",
				data: {
					service: "WFS",
					version: "1.1.0",
					request: "GetFeature",
					typename: "PythonAlergies:patiente_postgis",
					srsname: "EPSG:4326",
					outputFormat: "application/json",
					bbox: extent.join(",")+',EPSG:4326'
				}
			}).done(function(response,status){
				
				WFS_Patientes.getSource().addFeatures(new ol.format.GeoJSON().readFeatures(response));
			})
		},
		strategy: ol.loadingstrategy.bbox,
		projection: 'EPSG:4326'
	}),
	style: style_Patientes
});	

var format = new ol.format.GeoJSON();

// Ajax request 
$.ajax("http://localhost:8090/geoserver/wfs",{
	
	type : "GET",
	data : {
		service: "WFS",
		version: "1.0.0",
		request: 'GetFeature',
		typename: 'PythonAlergies:SRB_adm1',
		outputFormat: "JSON"
	}
}).done(function(data,b,c){
		
		format.readFeatures(data); 
		//console.log(format);
		
		$.each(data,function(index, value){
			console.log(value);
			if(index == "features"){
				$.each(value, function(k,v){
					console.log(v.properties.NAME_1); 
					var collapse = document.querySelector('#regionsPanel');
					var input = document.createElement('input');		
					input.type = 'checkbox';
					input.name = 'regions';
					input.id = v.properties.NAME_1;
					input.setAttribute('class','col-md-2');
					var label = document.createElement('label');
					label.setAttribute('class','col-md-10');
					label.appendChild(document.createTextNode(''+v.properties.NAME_1+''));
					label.appendChild(input);
					
					var div = document.createElement('div');	
					div.setAttribute('class','checkbox col-md-12');
					div.appendChild(label);
					div.appendChild(input);
					
					collapse.appendChild(div);
					
						
				})
				
				
			}
		})
});


var Osm = new ol.layer.Tile({
	name: 'Osm',
	visible:true,
	source: new ol.source.OSM()
	
});

var StamenToner= new ol.layer.Tile({
	name:"StamenToner",
	visible:false,
	source: new ol.source.Stamen({
		layer: 'toner'
	})
});

var StamenTerrain = new ol.layer.Tile({
	name:"StamenTerrain",
	visible:false,
	source: new ol.source.Stamen({
		layer: 'terrain'
	})
});

/************************************End Layer Definitions***********************************************/
/*######################################################################################################*/ 
/************************************Map Definition*******************************************************/
var map = new ol.Map({
	target: 'map',
	layers: [
		Osm,StamenToner,StamenTerrain,WFS_Borders, WFS_Patientes
	],
	controls: ol.control.defaults().extend([
		new ol.control.ScaleLine,
		new ol.control.ZoomSlider()
	]),
	view: new ol.View({
		projection: 'EPSG:4326',
		center: [21.7,45],
		zoom: 8,
	})
});
/***************************************************End Map Widget****************************************************/
/*###################################################################################################################*/
/**********************************************Overlay Popup*************************************************************/
// Overlay Popup With Layer Information 
var coords_field = $('#coords');
var address_field = $('#address');
var btnPatiente = $('#btFindPatiente');

function findPatienteBySubmit(){
	var coords = coords_field.val(); 
	var coords_array;
	
	if(coords.indexOf(",") != -1){
		coords_array = coords.split(",");
		return coords_array;
		
	}else if(coords.indexOf(" ") != -1){
		coords_array = coords.split(" ");
		
		return coords_array;
		
	}
	else {
		alert("You must divade coordinates by comma or space:((lat,lon)or (lat lon))");
		
	}
	
};

map.on('singleclick', function(evt){
	coords = evt.coordinate 
	var x = coords[0].toFixed(5);
	var y = coords[1].toFixed(5);
	var coords_str = ""+x+"  "+y 
	
	coords_field.val(coords_str);
	var address;
	var p = {};
	var name = map.forEachFeatureAtPixel(evt.pixel, function(feature, layer){
		var prop = feature.getProperties();
		address = feature.get('adresa');
		p = $.extend(true, {}, prop);
		return layer.get('name');
	});
	
	address_field.val(address);
	
	var i = "<table class='table table-bordered table-hover'>";
	$('#sln').text(name);
	$.each(p,function(k,v){
		if (k == "geometry") {
			return true;
		}
		i+="<tr><th>"+(k[0].toUpperCase()+k.slice(1))+"</th>"+"<td>"+v+"</td></tr>";
	});
	i+="</table>";
	content.innerHTML = i;
	overlay.setPosition(evt.coordinate);
	map.addOverlay(overlay);

});

// Create Overlay Popup 

var container = document.getElementById('popup');
var content = document.getElementById('popup-content');
var closer = document.getElementById('popup-closer');

$(closer).on('click',function(){
	overlay.setPosition(undefined);
	closer.blur();
	return false;
});

var overlay = new ol.Overlay({
	element: container,
	positioning: 'topp-center',
	autoPan: true,
	autoPanAnimation: {
		duration:250
	}

});
/***************************************************End Overlay Popup****************************************************/
/*###################################################################################################################*/
/*###########################################################################################################################*/
var lnums = document.querySelector('#lnums');
lnums.appendChild(document.createTextNode(''+map.getLayers().getLength()+'')) 

var zoom = document.querySelector('#zoom');
zoom.appendChild(document.createTextNode(''+map.getView().getZoom()+'')); 

// Change value of zoom field when change resolution of the map -->
map.getView().on('change:resolution',function(e){
	
	zoom.innerHTML = "";
	zoom.appendChild(document.createTextNode(''+map.getView().getZoom()+'')); 
});

var projection = document.querySelector('#projection');
projection.appendChild(document.createTextNode(''+map.getView().getProjection().getCode()+''));
// Change Display Layer When Click On Radio Button -->
$('input[type=radio]').on('change',function(){
	var radName = $(this).attr('name');
	var layer = $(this).val();
	map.getLayers().getArray().forEach(function(e){
		var name = e.get('name');
		if(radName == "base_layers"){
			alert("Djordje");
			e.setVisible(name == layer);
		}
});
		/*var layers = map.getLayers(); 
		layers.forEach(function(e){
			if(layer == e.get('name')){
				e.setVisible(true);
			}
			
		});*/
			
		
	});

//Geoserver rest workspaces 
/*
$.ajax("{% url 'alergies_maper:wr'%}",{
	type:"GET",
	headers:{'Accept':'application/json','Content-Type':'application/json'}
	
}).done(function(response, status){
	
	//alert(status);
	console.log("Response is: "+response);
	
}).fail(function(ob, status){
	//alert(status);
	for(var i in ob){
		console.log(i+":"+ob[i]);
	}
});*/


// Cluster Source -->
var features = [];

var source2 = new ol.source.Vector({
	
});

var format = new ol.format.GeoJSON();

//Clustering Layer Continuing
/*$.ajax("http://localhost:8090/geoserver/wfs",{
				type: "GET",
				data: {
					service: "WFS",
					version: "1.1.0",
					request: "GetFeature",
					typename: "PythonAlergies:patiente_postgis",
					srsname: "EPSG:4326",
					outputFormat: "application/json",
					
				}
			}).done(function(response,status){
				//alert(status)
				/*source2.addFeatures(new ol.format.GeoJSON().readFeatures(response));
				
				var source = new ol.source.Vector({
					features: source2.getFeatures(),
					projection: 'EPSG:4326'
				});

				var clusterSource = new ol.source.Cluster({
					distance: 8,
					projection: 'EPSG:4326',
					source: source
				});
				
				var clusters = new ol.layer.Vector({
					source: clusterSource
				})
				
				map.addLayer(clusterSource);
			});*/








});