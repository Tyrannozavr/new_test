function getStatus(taskID) {
  $.ajax({
    url: `/diagram_update/`,
    method: 'GET'
  })
                        .done((res) => {
// $(document).ready(function () {
$("#chart").shieldChart({
theme: "light",
primaryHeader: {
text: "Обзор бюджета"
},
exportOptions: {
image: false,
print: false
},
  axisX: {
   categoricalValues:
   // res.label
       ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]
},
tooltipSettings: {
       chartBound: true,
axisMarkers: {
enabled: true,
mode: 'xy'
}
},
dataSeries: [{
seriesType: 'line',
collectionAlias: "Бюджет в тысячaх",
data:
    // res.data
    [100, 320, 453, 234, 553, 665, 345, 123, 432, 545, 654, 345, 332, 456, 234]
}]
});
// });
// if (taskStatus === 'SUCCESS' || taskStatus === 'FAILURE') return false;
setTimeout(function() {
getStatus(res.task_id);
}, 10000);
})
  .fail((err) => {
    console.log(err)
  });
}
getStatus(1)