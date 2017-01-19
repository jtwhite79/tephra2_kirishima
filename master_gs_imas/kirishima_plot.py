import os
import numpy as np
import pylab

import kirishima_run as k_run
import kirishima_info as info

plt_dir = "plots"


def plot_locs(vals,ax):
    obs = info.obs_xys
    if vals is not None:
        ax.scatter(obs[:,0],obs[:,1],marker='.',s=vals*200,edgecolor="none")
    else:
        ax.scatter(obs[:,0],obs[:,1],marker='.',s=20,edgecolor="none",color='k')
    ax.scatter([info.vent_x],[info.vent_y],marker='^',color="k",s=20)
    ax.set_xlim(info.map_xlim)
    ax.set_ylim(info.map_ylim)
    return ax

def plot_obs_vs_sim_locs(case="reg"):

    res = info.load_rei(case)[0]
    #print res
    fig = pylab.figure(figsize=(10,20))
    ax_obs = pylab.subplot(311)
    ax_mod = pylab.subplot(312)
    ax_res = pylab.subplot(313)

    ax_obs = plot_locs(res["measured"]*res["weight"],ax_obs)
    ax_mod = plot_locs(res["modeled"]*res["weight"],ax_mod)
    res_vals = (res["measured"] - res["modeled"]) * res["weight"]
    #print res_vals.min(),res_vals.max()
    ax_res = plot_locs(res_vals,ax_res)
    pylab.savefig(os.path.join(plt_dir,"obs_vs_sim.png"))


def plot_obs_vs_sim_loe(case="reg"):
    res = info.load_rei(case)[0]
    fig = pylab.figure()
    ax = pylab.subplot(111)
    ax.scatter(res["modeled"],res["measured"],marker='.')
    ylim = ax.get_ylim()
    ax.plot(ylim,ylim,'k',lw=2.0)
    ax.set_xlim(ylim)
    ax.set_ylim(ylim)
    pylab.savefig(os.path.join(plt_dir,"loe.png"))

def plot_grid(case="reg",run=False):
    if run:
        info.write_grid()
        k_run.tephra(pts_file=info.grid_file,results_file=info.grid_results_file)

    #x = np.linspace(info.map_xlim[0],info.map_xlim[1],info.grid_step)
    #y = np.linspace(info.map_ylim[0],info.map_ylim[1],info.grid_step)

    grid = np.loadtxt(info.grid_results_file,skiprows=1,usecols=[0,1,3])
    res = info.load_rei(case)[0]

    arr = info.resize(grid[:,0],grid[:,1],grid[:,2])
    arr = np.log10(np.flipud(np.ma.masked_where(arr<=0.5,arr)))


    print arr.shape,arr.min(),arr.max()

    fig = pylab.figure()
    ax = pylab.subplot(1,1,1,aspect="equal")
    extent = [info.map_xlim[0],info.map_xlim[1],info.map_ylim[0],info.map_ylim[1]]
    im = ax.imshow(arr,interpolation="none",extent=extent,alpha=0.5,cmap="YlOrRd_r")
    #plot_locs(info.obs_xys[3,:],ax)
    #plot_locs((res["measured"]-res["modeled"])*res["weight"],ax)
    plot_locs(None,ax)
    pylab.colorbar(im,label="$log_{10}$ isomass")
    pylab.savefig(os.path.join(plt_dir,"grid.png"))


#plot_obs_vs_sim_locs()
plot_grid()
#plot_obs_vs_sim_loe()

