 
            $(document).ready(function() {
         $('#example').DataTable();
        } );



                         $(document).ready(function () {
                 $('#sidebarCollapse').on('click', function () {
                     $('#sidebar').toggleClass('active');
                 });
             });
    

        let draw = false;
          init();
          /**
           * FUNCTIONS
           */
          $(document).ready(function() {
          const tables = $('#example').DataTable( {
              "order": [[ 3, "desc" ]]
            } );
            mark: true
                      // get table data
            const tableDatas = getTableData(tables);
            // create Highcharts
            createHighcharts(tableDatas);
            // table events
            setTableEvents(tables);

          } );


          function init() {
            // initialize DataTables
            const tables = $("#dt-table").DataTable();
            mark: true
            // get table data
            const tableDatas = getTableData(tables);
            // create Highcharts
            createHighcharts(tableDatas);
            // table events
            setTableEvents(tables);
            
          }

          function getTableData(tables) {
            const dataArray = [],
              countryArray = [],
              populationArray = [],
              densityArray = [];

            // loop table rows
            table.rows({ search: "applied" }).every(function() {
              const data = this.data();
              countryArray.push(data[0]);
              populationArray.push(parseInt(data[6].replace(/\,/g, "")));
              densityArray.push(parseInt(data[4].replace(/\,/g, "")));
            });

            // store all data in dataArray
            dataArray.push(countryArray, populationArray, densityArray);

            return dataArray;
          }

          function createHighcharts(data) {
            Highcharts.setOptions({
              lang: {
                thousandsSep: ","
              }
            });

            Highcharts.chart("chart", {
              title: {
                text: "Cooperatives' Growth"
              },
              //subtitle: {
                //text: "Data from worldometers.info"
              //},
              xAxis: [
                {
                  categories: data[0],
                  labels: {
                    rotation: -45
                  }
                }
              ],
              yAxis: [
                {
                  // first yaxis
                  title: {
                    text: "Members (2017)"
                  }
                },
                {
                  // secondary yaxis
                  title: {
                    text: "Shares (P/member)"
                  },
                  min: 0,
                  opposite: true
                }
              ],
              series: [
                {
                  name: "Members (2017)",
                  color: "#0071A7",
                  type: "column",
                  data: data[1],
                  tooltip: {
                    valueSuffix: " Members"
                  }
                },
                {
                  name: "Shares (P/member)",
                  color: "#FF404E",
                  type: "spline",
                  data: data[2],
                  yAxis: 1
                }
              ],
              tooltip: {
                shared: true
              },
              legend: {
                backgroundColor: "#ececec",
                shadow: true
              },
              credits: {
                enabled: false
              },
              noData: {
                style: {
                  fontSize: "16px"
                }
              }
            });
          }

          function setTableEvents(tables) {
            // listen for page clicks
            tables.on("page", () => {
              draw = true;
            });

            // listen for updates and adjust the chart accordingly
            table.on("draw", () => {
              if (draw) {
                draw = false;
              } else {
                const tableDatas = getTableData(tables);
                createHighcharts(tableDatas);
              }
            });
          }









          function getTableData(table) {
            const dataArrays = [],
              countryArrays = [],
              populationArrays = [],
              densityArrays = [];

            // loop table rows
            table.rows({ search: "applied" }).every(function() {
              const data = this.data();
              countryArrays.push(data[1]);
              populationArrays.push(parseInt(data[0].replace(/\,/g, "")));
              densityArrays.push(parseInt(data[3].replace(/\,/g, "")));
            });

            // store all data in dataArray
            dataArrays.push(countryArrays, populationArrays, densityArrays);

            return dataArrays;
          }

          function createHighcharts(data) {
            Highcharts.setOptions({
              lang: {
                thousandsSep: ","
              }
            });

            Highcharts.chart("chartx", {
              title: {
                text: "Activities Logs"
              },
              //subtitle: {
                //text: "Data from worldometers.info"
              //},
              xAxis: [
                {
                  categories: data[0],
                  labels: {
                    rotation: -45
                  }
                }
              ],
              yAxis: [
                {
                  // first yaxis
                  title: {
                    text: "Members (2017)"
                  }
                },
                {
                  // secondary yaxis
                  title: {
                    text: "Shares (P/member)"
                  },
                  min: 0,
                  opposite: true
                }
              ],
              series: [
                {
                  name: "Members (2017)",
                  color: "#0071A7",
                  type: "column",
                  data: data[1],
                  tooltip: {
                    valueSuffix: " Members"
                  }
                },
                {
                  name: "Shares (P/member)",
                  color: "#FF404E",
                  type: "spline",
                  data: data[2],
                  yAxis: 1
                }
              ],
              tooltip: {
                shared: true
              },
              legend: {
                backgroundColor: "#ececec",
                shadow: true
              },
              credits: {
                enabled: false
              },
              noData: {
                style: {
                  fontSize: "16px"
                }
              }
            });
          }

          function setTableEvents(table) {
            // listen for page clicks
            table.on("page", () => {
              draw = true;
            });

            // listen for updates and adjust the chart accordingly
            table.on("draw", () => {
              if (draw) {
                draw = false;
              } else {
                const tableData = getTableData(table);
                createHighcharts(tableData);
              }
            });
          }