. build/envsetup.sh
export USE_CCACHE=1 && ccache -M 50G && export CONFIG_STATE_NOTIFIER=y 
lunch legion_X00TD-user
make legion