from re import sub
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

cps_df = pd.read_csv('clean_data/cellphones.csv')
tgdd_df = pd.read_csv('clean_data/tgdd.csv')
tiki_df = pd.read_csv('clean_data/tiki.csv')
vt_df = pd.read_csv('clean_data/viettel.csv')
ddv_df = pd.read_csv('clean_data/didongviet.csv')
dmx_df = pd.read_csv('clean_data/dienmayxanh.csv')
final_df = pd.read_csv('clean_data/final_data.csv')

cps_map = pd.read_csv('matcher/cps_map.csv')
tgdd_map = pd.read_csv('matcher/tgdd_map.csv')
tiki_map = pd.read_csv('matcher/tiki_map.csv')
vt_map = pd.read_csv('matcher/vt_map.csv')
ddv_map = pd.read_csv('matcher/ddv_map.csv')
dmx_map = pd.read_csv('matcher/dmx_map.csv')

@app.route("/", methods=["GET", "POST"])
def main():
    # if request.method == "POST":
    #     ram = request.form.get("ram")
    #     return redirect(url_for('result', df=final_df.head(3)))
    return render_template("home.html", df=final_df)

@app.route("/result", methods=["GET", "POST"])
def result():
    res_df = final_df

    subname = request.form["subname"].lower()
    res_df = res_df[res_df['ten'].str.lower().str.contains(subname.lower())]

    ram = request.form.get("ram")
    if ram == 'under2':
        res_df = res_df[(res_df['ram'] > 0) & (res_df['ram'] < 2)]
    elif ram =='2to4':
        res_df = res_df[(res_df['ram'] >= 2) & (res_df['ram'] < 4)]
    elif ram == '4to8':
        res_df = res_df[(res_df['ram'] >= 4) & (res_df['ram'] < 8)]
    elif ram == '8to16':
        res_df = res_df[(res_df['ram'] >= 8) & (res_df['ram'] < 16)]
    elif ram == 'over16':
        res_df = res_df[res_df['ram'] >= 16]
    
    bo_nho_trong = request.form.get("bo_nho_trong")
    if bo_nho_trong == 'under32':
        res_df = res_df[(res_df['bo_nho_trong'] > 0) & (res_df['bo_nho_trong'] < 32)]
    elif bo_nho_trong == '32to64':
        res_df = res_df[(res_df['bo_nho_trong'] >= 32) & res_df['bo_nho_trong'] < 64]
    elif bo_nho_trong == '64to128':
        res_df = res_df[(res_df['bo_nho_trong'] >= 64) & res_df['bo_nho_trong'] < 128]
    elif bo_nho_trong == '128to512':
        res_df = res_df[(res_df['bo_nho_trong'] >= 128) & res_df['bo_nho_trong'] < 512]
    elif bo_nho_trong == 'over512':
        res_df = res_df[res_df['bo_nho_trong'] > 512]

    kich_thuoc_man_hinh = request.form.get("kich_thuoc_man_hinh")
    if kich_thuoc_man_hinh == 'under2':
        res_df = res_df[(res_df['kich_thuoc_man_hinh'] > 0) & (res_df['kich_thuoc_man_hinh'] < 2)]
    elif kich_thuoc_man_hinh == '2to4':
        res_df = res_df[(res_df['kich_thuoc_man_hinh'] >= 2) & (res_df['kich_thuoc_man_hinh'] < 4)]
    elif kich_thuoc_man_hinh == '4to6':
        res_df = res_df[(res_df['kich_thuoc_man_hinh'] >= 4) & (res_df['kich_thuoc_man_hinh'] < 6)]
    elif kich_thuoc_man_hinh == '6to8':
        res_df = res_df[(res_df['kich_thuoc_man_hinh'] >= 6) & (res_df['kich_thuoc_man_hinh'] < 8)]
    elif kich_thuoc_man_hinh == 'over8':
        res_df = res_df[res_df['kich_thuoc_man_hinh'] >= 8]
    
    return render_template("home.html", df=res_df)

@app.route("/record/<variable>", methods=["GET", "POST"])
def record(variable):
    schema_id = int(variable)
    name = final_df[final_df['id']==schema_id]['ten'].tolist()[0]

    cps_id = cps_map[cps_map['schema_id']==schema_id]['src_id'].tolist()
    res_cps_df = cps_df.loc[cps_df['id'].isin(cps_id)]
    res_cps_df['cua_hang'] = "CellphoneS"
    
    tgdd_id = tgdd_map[tgdd_map['schema_id']==schema_id]['src_id'].tolist()
    res_tgdd_df = tgdd_df.loc[tgdd_df['id'].isin(tgdd_id)]
    res_tgdd_df['cua_hang'] = "Thế giới di động"

    tiki_id = tiki_map[tiki_map['schema_id']==schema_id]['src_id'].tolist()
    res_tiki_df = tiki_df.loc[tiki_df['id'].isin(tiki_id)]
    res_tiki_df['cua_hang'] = "Tiki"

    vt_id = vt_map[vt_map['schema_id']==schema_id]['src_id'].tolist()
    res_vt_df = vt_df.loc[vt_df['id'].isin(vt_id)]
    res_vt_df['cua_hang'] = "Viettel Store"

    ddv_id = ddv_map[ddv_map['schema_id']==schema_id]['src_id'].tolist()
    res_ddv_df = ddv_df.loc[ddv_df['id'].isin(ddv_id)]
    res_ddv_df['cua_hang'] = "Di động Việt"

    dmx_id = dmx_map[dmx_map['schema_id']==schema_id]['src_id'].tolist()
    res_dmx_df = dmx_df.loc[dmx_df['id'].isin(dmx_id)]
    res_dmx_df['cua_hang'] = "Điện máy xanh"

    res_df = pd.concat([res_tgdd_df, res_cps_df, res_tiki_df, res_vt_df, res_ddv_df, res_dmx_df])
    return render_template("record.html", name=name, df=res_df)


if __name__ == "__main__":
    app.run(debug=True)
