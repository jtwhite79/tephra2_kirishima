import pst_handler as phand

pst = phand.pst("reg.pst")
#pst.proportional_weights(0.3,0.5)
obs = pst.observation_data
obs.index = obs.obgnme
imas_grp = obs.groupby(lambda x : "imas" in x.lower()).groups
obs.weight.loc[imas_grp[False]] = 0.0
obs.index = obs.obsnme
big_groups = obs.groupby(lambda x: x.startswith("ks062") or x.startswith("mb004")).groups
obs.weight.loc[big_groups[True]] = 0.0
obs = obs.sort(["obgnme","obsval"])
pst.observation_data = obs
pst.zero_order_tikhonov()
pst.write("reg_imas.pst",True)

pst = phand.pst("reg.pst")
#pst.proportional_weights(0.25,1.0)
obs = pst.observation_data
obs.index = obs.obgnme
imas_grp = obs.groupby(lambda x : "imas" in x.lower()).groups
obs.weight.loc[imas_grp[True]] = 0.0
obs.index = obs.obsnme
big_groups = obs.groupby(lambda x: x.startswith("ks062") or x.startswith("mb004")).groups
obs.weight.loc[big_groups[True]] = 0.0
obs = obs.sort(["obgnme","obsval"])
pst.observation_data = obs
pst.zero_order_tikhonov()
pst.write("reg_gs.pst",True)

pst = phand.pst("reg.pst")
pst.proportional_weights(0.25,0.25)
obs = pst.observation_data
obs.index = obs.obgnme
imas_grp = obs.groupby(lambda x : "imas_2" in x.lower()).groups
obs.weight.loc[imas_grp[True]] = 0.0
obs.index = obs.obsnme
big_groups = obs.groupby(lambda x: x.startswith("ks062") or x.startswith("mb004")).groups
obs.weight.loc[big_groups[True]] = 0.0
obs = obs.sort(["obgnme","obsval"])
pst.observation_data = obs
pst.zero_order_tikhonov()
pst.write("reg_base.pst",True)

pst = phand.pst("reg.pst")
pst.proportional_weights(0.25,0.25)
obs = pst.observation_data
obs.index = obs.obgnme
imas_grp = obs.groupby(lambda x : "imas_2" in x.lower()).groups
obs.weight.loc[imas_grp[True]] = 0.0
imas_grp = obs.groupby(lambda x : "gs" in x.lower()).groups
obs.weight.loc[imas_grp[True]] = 0.0

obs.index = obs.obsnme
big_groups = obs.groupby(lambda x: x.startswith("ks062") or x.startswith("mb004")).groups
obs.weight.loc[big_groups[True]] = 0.0
obs = obs.sort(["obgnme","obsval"])
pst.observation_data = obs
pst.zero_order_tikhonov()
pst.write("reg_base_imas.pst",True)
