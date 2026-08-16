/** AXIS AUTOMATED MANIFEST CONSUMPTION ENGINE */
function onOpen() {
  SpreadsheetApp.getUi().createMenu("𖤐 AXIS ENGINE").addItem("Ingest Remote Manifest", "fetchAndRenderManifest").addToUi();
}
function fetchAndRenderManifest() {
  const repoUrl = "https://raw.githubusercontent.com/SUPRANODE00/SL1TH3R-RAINBOW/main/sl1th3r_rainbow_manifest.json";
  try {
    const response = UrlFetchApp.fetch(repoUrl);
    const jsonText = response.getContentText();
    const manifest = JSON.parse(jsonText);
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let mainSheet = ss.getSheetByName("StateGrid_Manifest") || ss.insertSheet("StateGrid_Manifest");
    mainSheet.clear();
    mainSheet.getRange("A1:C1").merge().setValue("AXIS TECHNICAL STATE-GRID LOG // THE SAW IS THE LAW").setFontColor("#ffffff").setBackgroundColor("#7a0000").setFontWeight("bold").setFontSize(12).setHorizontalAlignment("center");
    mainSheet.getRange("A2:C2").setValues([["IDENTIFIER SYSTEM", "METRIC BLOCK", "VALUE VALUE"]]).setFontWeight("bold").setBackgroundColor("#0b0b0b").setFontColor("#ffffff");
    const model = manifest.state_grid_autonomy_model;
    const anchor = model.spatial_anchor;
    const pipeline = model.openusd_hydra_pipeline;
    const rows = [
      ["SUPRANODE00", "Identity Token", model.system_identity],
      ["SUPRANODE00", "Signature Authority", model.signature_authority],
      ["SUPRANODE00", "Anchor Vertex Latitude", anchor.vertex_lat.toString()],
      ["SUPRANODE00", "Anchor Vertex Longitude", anchor.vertex_lon.toString()],
      ["SUPRANODE00", "H3 Hexagonal Index Location", anchor.h3_index],
      ["SUPRANODE00", "Geospatial Coordinate Datum", anchor.coordinate_datum],
      ["SUPRANODE00", "OpenUSD Rendering Core", pipeline.imaging_plugin],
      ["SUPRANODE00", "RenderMan Environment Root", pipeline.environment_routing.RMANTREE],
      ["SUPRANODE00", "Custom Schema Mapping Node ID", pipeline.custom_schema_domains["primvars:axis:nodeId"]],
      ["SUPRANODE00", "System Synchronization State", pipeline.custom_schema_domains["primvars:axis:systemState"]],
      ["SUPRANODE00", "Operational Speed / Cadence", "Whitechapel: Section 6 Alignment Locked"]
    ];
    mainSheet.getRange(3, 1, rows.length, 3).setValues(rows);
    mainSheet.autoResizeColumns(1, 3);
    mainSheet.getRange(13, 3).setBackgroundColor("#1c3b1e").setFontColor("#4ffc61").setFontWeight("bold");
    SpreadsheetApp.getUi().alert("𖤐 STATE-GRID INGESTION COMPLETE.");
  } catch (error) {
    SpreadsheetApp.getUi().alert("Synchronization Error.");
  }
}
