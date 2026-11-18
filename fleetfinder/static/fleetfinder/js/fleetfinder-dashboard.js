/* global aaFleetFinderSettings, aaFleetFinderSettingsOverride, objectDeepMerge, fetchGet, fleetfinderBootstrapTooltip, DataTable, _removeSearchFromColumnControl */

$(document).ready(() => {
    'use strict';

    const fleetFinderSettings = objectDeepMerge(aaFleetFinderSettings, aaFleetFinderSettingsOverride);

    const table_fleet_overview = $('#table_available-fleets');
    let dataTable = null;

    const dtColumn = {
        fleet_commander: 0,
        fleet_name: 1,
        created_at: 2,
        actions: 3
    };

    /**
     * Initialize or update the datatable.
     * If the table already exists, it will be updated with new data.
     * If it does not exist, a new DataTable will be created.
     *
     * @param {Object} data - The fleet data to populate the table.
     */
    const initializeOrUpdateTable = (data) => {
        if (dataTable) {
            // Update existing table
            dataTable.clear().rows.add(data).draw();
        } else {
            // Initialize new table
            dataTable = new DataTable(table_fleet_overview, {
                ...fleetFinderSettings.dataTables,
                data: data,
                columns: [
                    {
                        data: 'fleet_commander',
                        render: {
                            _: 'html',
                            sort: 'sort'
                        }
                    },
                    {
                        data: 'fleet_name'
                    },
                    {
                        data: 'created_at'
                    },
                    {
                        data: 'actions',
                        className: 'text-end'
                    }
                ],
                columnDefs: [
                    {
                        target: dtColumn.created_at,
                        render: DataTable.render.date(
                            fleetFinderSettings.dataTables.datetimeFormat
                        ),
                        columnControl: _removeSearchFromColumnControl(fleetFinderSettings.dataTables.columnControl, 1)
                    },
                    {
                        target: dtColumn.actions,
                        columnControl: [
                            {target: 0, content: []},
                            {target: 1, content: []}
                        ],
                        orderable: false,
                        width: 135
                    }
                ],
                order: [[dtColumn.fleet_commander, 'asc']],
                paging: false,
                initComplete: () => {
                    // Get DataTable instance
                    const dt = table_fleet_overview.DataTable();

                    // Initialize Bootstrap tooltips
                    fleetfinderBootstrapTooltip({selector: '#table_available-fleets'});

                    // Re-initialize tooltips on each draw
                    dt.on('draw', () => {
                        fleetfinderBootstrapTooltip({selector: '#table_available-fleets'});
                    });
                }
            });
        }
    };

    /**
     * Fetch and update fleet data
     */
    const fetchFleetData = () => {
        fetchGet({url: fleetFinderSettings.dataTables.url.dashboard})
            .then(initializeOrUpdateTable)
            .catch((error) => {
                console.error('Error fetching fleet data:', error);
            });
    };

    // Initial load
    fetchFleetData();

    // Refresh every 30 seconds
    setInterval(fetchFleetData, 30000);
});
