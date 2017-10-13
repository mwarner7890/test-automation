import adb
import unittest
from unittest.mock import MagicMock


class TestAdbGetDeviceProp(unittest.TestCase):
    def setUp(self):
        adb.Adb._call_adb_cmd_silently = MagicMock(return_value=None)
        adb.Adb.get_screen_resolution = MagicMock(return_value=None)

    def test_get_device_prop(self):
        adb.get_stdout_from_adb_command = MagicMock(return_value="""
    [af.music.outputid]: [3]
    [bgw.current3gband]: [0]
    [camera.disable_zsl_mode]: [1]
    [cdma.ril.ecclist]: []
    [cdma.ril.ecclist1]: []
    [dalvik.vm.appimageformat]: [lz4]
    [dalvik.vm.dex2oat-Xms]: [64m]
    [dalvik.vm.dex2oat-Xmx]: [512m]
    [dalvik.vm.heapgrowthlimit]: [192m]
    [dalvik.vm.heapsize]: [384m]
    [dalvik.vm.image-dex2oat-Xms]: [64m]
    [dalvik.vm.image-dex2oat-Xmx]: [64m]
    [dalvik.vm.isa.arm.features]: [default]
    [dalvik.vm.isa.arm.variant]: [cortex-a53]
    [dalvik.vm.isa.arm64.features]: [default]
    [dalvik.vm.isa.arm64.variant]: [cortex-a53]
    [dalvik.vm.mtk-stack-trace-file]: [/data/anr/mtk_traces.txt]
    [dalvik.vm.stack-trace-file]: [/data/anr/traces.txt]
    [dalvik.vm.usejit]: [true]
    [dalvik.vm.usejitprofiles]: [true]
    [debug.MB.running]: [0]
    [debug.atrace.tags.enableflags]: [0]
    [debug.cei.erb.ss]: [Started]
    [debug.force_rtl]: [0]
    [debug.hwc.bq_count]: [4]
    [debug.hwc.compose_level]: [0]
    [debug.mdlogger.Running]: [0]
    [debug.mdlogger.log2sd.path]: [internal_sd]
    [debug.mtk.aee.status]: [free]
    [debug.mtk.aee.status64]: [free]
    [debug.mtklog.netlog.Running]: [0]
    [dev.bootcomplete]: [1]
    [drm.service.enabled]: [true]
    [fmradio.driver.enable]: [1]
    [gsm.baseband.capability]: [1023]
    [gsm.current.phone-type]: [1,1]
    [gsm.defaultpdpcontext.active]: [true]
    [gsm.gcf.testmode]: [0]
    [gsm.lte.ca.support]: [1]
    [gsm.network.type]: [LTE,Unknown]
    [gsm.nitz.time]: [1507105138009]
    [gsm.operator.alpha]: [vodafone UK]
    [gsm.operator.alpha.2]: []
    [gsm.operator.iso-country]: [gb]
    [gsm.operator.isroaming]: [false,false]
    [gsm.operator.numeric]: [23415]
    [gsm.project.baseband]: [CCI6757_65_N(LWCTG_MP5)]
    [gsm.project.baseband.2]: [CCI6757_65_N(LWCTG_MP5)]
    [gsm.ril.ct3g]: [0]
    [gsm.ril.ct3g.2]: [0]
    [gsm.ril.eboot]: [-1]
    [gsm.ril.init]: [1]
    [gsm.ril.sst.mccmnc]: [23415]
    [gsm.ril.uicctype]: [USIM]
    [gsm.ril.uicctype.2]: [USIM]
    [gsm.serial]: [730881457B2                                                    ]
    [gsm.sim.operator.alpha]: [vodafone UK]
    [gsm.sim.operator.default-name]: [vodafone UK]
    [gsm.sim.operator.imsi]: [234159187373394]
    [gsm.sim.operator.iso-country]: [gb]
    [gsm.sim.operator.numeric]: [23415]
    [gsm.sim.retry.pin1]: [3]
    [gsm.sim.retry.pin1.2]: []
    [gsm.sim.retry.pin2]: [3]
    [gsm.sim.retry.pin2.2]: []
    [gsm.sim.retry.puk1]: [10]
    [gsm.sim.retry.puk1.2]: []
    [gsm.sim.retry.puk2]: [10]
    [gsm.sim.retry.puk2.2]: []
    [gsm.sim.ril.mcc.mnc]: []
    [gsm.sim.ril.mcc.mnc.2]: []
    [gsm.sim.ril.phbready]: [true]
    [gsm.sim.ril.phbready.2]: []
    [gsm.sim.ril.testsim]: [0]
    [gsm.sim.state]: [READY,ABSENT]
    [gsm.stkapp.name]: [Vodafone]
    [gsm.version.baseband]: [MOLY.LR11.W1630.MD.MP.V9.3.P25, 2017/09/19 18:57]
    [gsm.version.baseband1]: [MOLY.LR11.W1630.MD.MP.V9.3.P25, 2017/09/19 18:57]
    [gsm.version.ril-impl]: [android reference-ril 1.0]
    [init.svc.MPED]: [running]
    [init.svc.MtkCodecService]: [running]
    [init.svc.NvRAMAgent]: [running]
    [init.svc.aal]: [running]
    [init.svc.adbd]: [running]
    [init.svc.agpsd]: [running]
    [init.svc.audioserver]: [running]
    [init.svc.batterywarning]: [running]
    [init.svc.bootanim]: [stopped]
    [init.svc.cameraserver]: [running]
    [init.svc.ccci3_fsd]: [stopped]
    [init.svc.ccci3_mdinit]: [stopped]
    [init.svc.ccci_fsd]: [running]
    [init.svc.ccci_mdinit]: [running]
    [init.svc.clear-bcb]: [stopped]
    [init.svc.debuggerd]: [running]
    [init.svc.debuggerd64]: [running]
    [init.svc.drm]: [running]
    [init.svc.emdlogger1]: [running]
    [init.svc.emsvr_user]: [running]
    [init.svc.enableswap]: [stopped]
    [init.svc.epdg_wod]: [running]
    [init.svc.flash_recovery]: [stopped]
    [init.svc.fuelgauged]: [running]
    [init.svc.fuelgauged_nvram]: [stopped]
    [init.svc.gatekeeperd]: [running]
    [init.svc.ged_srv]: [running]
    [init.svc.gmadfs]: [running]
    [init.svc.gsm0710muxd]: [running]
    [init.svc.healthd]: [running]
    [init.svc.installd]: [running]
    [init.svc.ipsec_mon]: [running]
    [init.svc.keystore]: [running]
    [init.svc.lmkd]: [running]
    [init.svc.logd]: [running]
    [init.svc.logd-reinit]: [stopped]
    [init.svc.mal-daemon]: [running]
    [init.svc.media]: [running]
    [init.svc.mediacodec]: [running]
    [init.svc.mediadrm]: [running]
    [init.svc.mediaextractor]: [running]
    [init.svc.mnld]: [running]
    [init.svc.mobile_log_d]: [running]
    [init.svc.msensord]: [stopped]
    [init.svc.netd]: [running]
    [init.svc.netdiag]: [running]
    [init.svc.nvram_daemon]: [stopped]
    [init.svc.p2p_supplicant]: [running]
    [init.svc.pl_calibration]: [stopped]
    [init.svc.poweroff]: [stopped]
    [init.svc.pq]: [running]
    [init.svc.program_binary]: [running]
    [init.svc.ril-daemon-mtk]: [running]
    [init.svc.ril-proxy]: [running]
    [init.svc.servicemanager]: [running]
    [init.svc.slpd]: [running]
    [init.svc.smartpa_nv]: [stopped]
    [init.svc.spm_script]: [stopped]
    [init.svc.start_modem]: [stopped]
    [init.svc.surfaceflinger]: [running]
    [init.svc.sysenv_daemon]: [running]
    [init.svc.teei_daemon]: [running]
    [init.svc.terservice]: [stopped]
    [init.svc.tft_count]: [running]
    [init.svc.tft_data]: [stopped]
    [init.svc.tft_predata]: [stopped]
    [init.svc.thermal]: [running]
    [init.svc.thermal_manager]: [stopped]
    [init.svc.thermald]: [running]
    [init.svc.thermalloadalgod]: [running]
    [init.svc.ueventd]: [running]
    [init.svc.vold]: [running]
    [init.svc.vtservice]: [running]
    [init.svc.wifi2agps]: [running]
    [init.svc.wmt_launcher]: [running]
    [init.svc.wmt_loader]: [stopped]
    [init.svc.zygote]: [running]
    [init.svc.zygote_secondary]: [running]
    [log.tag]: [I]
    [log.tag.WifiHW]: [W]
    [media.wfd.portrait]: [0]
    [media.wfd.video-format]: [7]
    [mediatek.wlan.chip]: [CONSYS_MT6757]
    [mediatek.wlan.ctia]: [0]
    [mediatek.wlan.module.postfix]: [_consys_mt6757]
    [mtk.eccci.c2k]: [enabled]
    [mtk.md1.status]: [ready]
    [mtk.vdec.waitkeyframeforplay]: [1]
    [mtk_wifi.fwpath]: [STA]
    [mtknfc.status.type]: [unknow]
    [net.bt.name]: [Android]
    [net.change]: [net.dns1]
    [net.dns1]: [10.203.64.1]
    [net.hostname]: [android-2c9b4ea650fb02b3]
    [net.ims.ipsec.version]: [2.0]
    [net.nsiot_pending]: [false]
    [net.perf.cpu.core]: [4,4,0,0]
    [net.perf.cpu.freq]: [1183000,1638000,0,0]
    [net.perf.rps]: [ff]
    [net.qtaguid_enabled]: [1]
    [net.tcp.default_init_rwnd]: [60]
    [persist.af.hac_on]: [0]
    [persist.datashaping.alarmgroup]: [1]
    [persist.log.tag]: [I]
    [persist.log.tag.AEE_AED]: [D]
    [persist.log.tag.AT]: [I]
    [persist.log.tag.ActivityManager]: [D]
    [persist.log.tag.AndroidRuntime]: [D]
    [persist.log.tag.CdmaMoSms]: [I]
    [persist.log.tag.CdmaMtSms]: [I]
    [persist.log.tag.MAL-RDS]: [W]
    [persist.log.tag.MountService]: [D]
    [persist.log.tag.PackageManager]: [D]
    [persist.log.tag.RILC]: [I]
    [persist.log.tag.RILC-MTK]: [I]
    [persist.log.tag.RILC-RP]: [I]
    [persist.log.tag.RILJ]: [D]
    [persist.log.tag.RILMUXD]: [I]
    [persist.log.tag.RfxController]: [I]
    [persist.log.tag.RfxMainThread]: [I]
    [persist.log.tag.RfxRilAdapter]: [I]
    [persist.log.tag.RfxRoot]: [I]
    [persist.log.tag.ServiceThread]: [D]
    [persist.log.tag.ShutdownThread]: [D]
    [persist.log.tag.Watchdog]: [D]
    [persist.log.tag.WindowManager]: [D]
    [persist.log.tag.tel_log_ctrl]: [1]
    [persist.log.tag.wmt_launcher]: [W]
    [persist.logd.size]: []
    [persist.meta.dumpdata]: [0]
    [persist.mtk.connsys.poweron.ctl]: [0]
    [persist.mtk.datashaping.support]: [1]
    [persist.mtk.wcn.combo.chipid]: [0x6757]
    [persist.mtk.wcn.dynamic.dump]: [0]
    [persist.mtk.wcn.patch.version]: [20170524173704a]
    [persist.mtk_dynamic_ims_switch]: [0]
    [persist.mtk_epdg_support]: [1]
    [persist.mtk_nlp_switch_support]: [1]
    [persist.mtk_vilte_support]: [0]
    [persist.radio.cfu.change.0]: [0]
    [persist.radio.cfu.iccid.0]: [89441000302497337501]
    [persist.radio.cfu.timeslot.0]: []
    [persist.radio.data.iccid]: [89441000302497337501]
    [persist.radio.default.sim]: [0]
    [persist.radio.fd.counter]: [150]
    [persist.radio.fd.off.counter]: [50]
    [persist.radio.fd.off.r8.counter]: [50]
    [persist.radio.fd.r8.counter]: [150]
    [persist.radio.ia]: []
    [persist.radio.ia-apn]: []
    [persist.radio.ia-pwd-flag]: [1]
    [persist.radio.lte.chip]: [1]
    [persist.radio.mobile.data]: [89441000302497337501,N/A]
    [persist.radio.mtk_dsbp_support]: [1]
    [persist.radio.mtk_ps2_rat]: [W/G]
    [persist.radio.mtk_ps3_rat]: [G]
    [persist.radio.multisim.config]: [dsds]
    [persist.radio.new.sim.slot]: []
    [persist.radio.re.ia-apn]: []
    [persist.radio.re.ia.flag]: [0]
    [persist.radio.reset_on_switch]: [false]
    [persist.radio.sim.sbp]: [6]
    [persist.radio.sim.status]: []
    [persist.radio.simswitch]: [1]
    [persist.radio.simswitch.iccid]: [89441000302497337501]
    [persist.radio.terminal-based.cw]: [disabled_tbcw]
    [persist.radio.unlock]: [false]
    [persist.radio.ut.cfu.mode]: [enabled_ut_cfu_mode_off]
    [persist.service.acm.enable]: [0]
    [persist.service.bdroid.bdaddr]: [22:22:59:cd:91:f8]
    [persist.service.stk.shutdown]: [0]
    [persist.sys.bluelight.default]: [128]
    [persist.sys.dalvik.vm.lib.2]: [libart.so]
    [persist.sys.first_time_boot]: [false]
    [persist.sys.locale]: [en-US]
    [persist.sys.mute.state]: [1]
    [persist.sys.pq.adl.idx]: [0]
    [persist.sys.pq.iso.shp.en]: [1]
    [persist.sys.pq.log.en]: [0]
    [persist.sys.pq.mdp.color.dbg]: [1]
    [persist.sys.pq.mdp.color.idx]: [0]
    [persist.sys.pq.shp.idx]: [2]
    [persist.sys.pq.ultrares.en]: [1]
    [persist.sys.profiler_ms]: [0]
    [persist.sys.sd.defaultpath]: [/storage/emulated/0]
    [persist.sys.timezone]: [Europe/London]
    [persist.sys.underwater]: [0]
    [persist.sys.usb.config]: [mtp,adb]
    [persist.sys.webview.vmsize]: [113626032]
    [pm.dexopt.ab-ota]: [speed-profile]
    [pm.dexopt.bg-dexopt]: [speed-profile]
    [pm.dexopt.boot]: [verify-profile]
    [pm.dexopt.core-app]: [speed]
    [pm.dexopt.first-boot]: [interpret-only]
    [pm.dexopt.forced-dexopt]: [speed]
    [pm.dexopt.install]: [interpret-only]
    [pm.dexopt.nsys-library]: [speed]
    [pm.dexopt.shared-apk]: [speed]
    [qemu.hw.mainkeys]: [1]
    [ril.active.md]: [14]
    [ril.attach.sim]: [0]
    [ril.c2kirat.ia]: [89441000302497337501,internet]
    [ril.cdma.card.type.1]: []
    [ril.cdma.card.type.2]: []
    [ril.cdma.switching]: [0]
    [ril.data.mal]: [0]
    [ril.ecclist]: [999,23;112,23;911,31;112,0;911,0]
    [ril.ecclist1]: []
    [ril.external.md]: [0]
    [ril.fd.mode]: [1]
    [ril.first.md]: [1]
    [ril.flightmode.poweroffMD]: [0]
    [ril.ia.iccid]: [89441000302497337501]
    [ril.ia.network]: [internet.mnc015.mcc234.gprs]
    [ril.iccid.sim1]: [89441000302497337501]
    [ril.iccid.sim2]: [N/A]
    [ril.imsi.status.sim1]: [1]
    [ril.imsi.status.sim2]: [0]
    [ril.ipo.radiooff]: [0]
    [ril.ipo.radiooff.2]: [0]
    [ril.mal.flag]: [0]
    [ril.mal.socket]: [rilproxy-mal]
    [ril.mux.ee.md1]: [0]
    [ril.mux.report.case]: [0]
    [ril.nw.erat.ext.support]: [1]
    [ril.nw.worldmode.activemode]: [1]
    [ril.pdn.reuse]: [1]
    [ril.phone1.mapped.md]: [MD1]
    [ril.pid.1]: [1104]
    [ril.radio.ia]: [89441000302497337501,IP,-1,web,0]
    [ril.radio.ia-apn]: [internet]
    [ril.radiooff.poweroffMD]: [0]
    [ril.read.imsi]: [1]
    [ril.ready.sim]: [true]
    [ril.rilproxy]: [1]
    [ril.sim.type]: []
    [ril.specific.sm_cause]: [0]
    [ril.telephony.mode]: [0]
    [ril.uim.subscriberid.1]: []
    [ril.uim.subscriberid.2]: []
    [ril.volte.mal.latency]: [65535]
    [ril.volte.mal.opkey]: [0x0002]
    [ril.volte.mal.pkterrth]: [99]
    [ril.volte.mal.rb_hoddc_t]: [3]
    [ril.volte.mal.rb_hol2w_t]: [10]
    [ril.volte.mal.rb_how2l_t]: [150]
    [ril.volte.mal.retranth]: [99]
    [ril.volte.mal.throupt]: [65535]
    [ril.volte.mal.vijit]: [3]
    [ril.volte.mal.vojit]: [26]
    [rild.libargs]: [-d /dev/ttyC0]
    [rild.libpath]: [mtk-ril.so]
    [rild.mark_switchuser]: [0]
    [ro.adb.secure]: [1]
    [ro.aee.enperf]: [off]
    [ro.allow.mock.location]: [0]
    [ro.audio.silent]: [0]
    [ro.baseband]: [unknown]
    [ro.board.platform]: [mt6757]
    [ro.boot.bootreason]: [power_key]
    [ro.boot.cid]: [EUR]
    [ro.boot.flash.locked]: [1]
    [ro.boot.hardware]: [mt6757]
    [ro.boot.mode]: [normal]
    [ro.boot.opt_c2k_lte_mode]: [0]
    [ro.boot.opt_c2k_support]: [0]
    [ro.boot.opt_eccci_c2k]: [1]
    [ro.boot.opt_irat_support]: [0]
    [ro.boot.opt_lte_support]: [1]
    [ro.boot.opt_md1_support]: [14]
    [ro.boot.opt_md3_support]: [0]
    [ro.boot.opt_ps1_rat]: [Lf/W/G]
    [ro.boot.opt_using_default]: [1]
    [ro.boot.sbc_enabled]: [1]
    [ro.boot.serialno]: [S411719005315]
    [ro.boot.verifiedbootstate]: [green]
    [ro.bootimage.build.date]: [Tue Sep 19 19:44:18 CST 2017]
    [ro.bootimage.build.date.utc]: [1505821458]
    [ro.bootimage.build.fingerprint]: [Cat/CatS41/CatS41:7.0/NRD90M/LTE_D0201121.0_S41_0.023.01:user/release-keys]
    [ro.bootloader]: [unknown]
    [ro.bootmode]: [normal]
    [ro.build.cei_factory]: [0]
    [ro.build.characteristics]: [default]
    [ro.build.date]: [Tue Sep 19 19:44:18 CST 2017]
    [ro.build.date.utc]: [1505821458]
    [ro.build.description]: [full_cci6757_65_n-user 7.0 NRD90M 1505821484 release-keys]
    [ro.build.display.id]: [LTE_D0201121.0_S41_0.023.01]
    [ro.build.fingerprint]: [Cat/CatS41/CatS41:7.0/NRD90M/LTE_D0201121.0_S41_0.023.01:user/release-keys]
    [ro.build.flavor]: [CatS41-user]
    [ro.build.host]: [vBuild1CT41]
    [ro.build.id]: [NRD90M]
    [ro.build.product]: [CatS41]
    [ro.build.sku]: [DT]
    [ro.build.tags]: [release-keys]
    [ro.build.type]: [user]
    [ro.build.user]: [rdadmin]
    [ro.build.version.all_codenames]: [REL]
    [ro.build.version.base_os]: []
    [ro.build.version.codename]: [REL]
    [ro.build.version.incremental]: [1505821484]
    [ro.build.version.preview_sdk]: [0]
    [ro.build.version.release]: [7.0]
    [ro.build.version.sdk]: [24]
    [ro.build.version.security_patch]: [2017-08-05]
    [ro.build.version.software]: [LTE_D0201121.0_S41_0.023.01]
    [ro.camera.sound.forced]: [0]
    [ro.carrier]: [unknown]
    [ro.cei.ftm_pin]: [0]
    [ro.cei.hw_id]: [DVT2]
    [ro.cei.proj_id]: [CT41]
    [ro.com.android.mobiledata]: [true]
    [ro.com.google.clientidbase]: [android-bullitt]
    [ro.com.google.gmsversion]: [7.0_r9]
    [ro.config.alarm_alert]: [Alarm_Classic.ogg]
    [ro.config.notification_sound]: [pixiedust.ogg]
    [ro.config.ringtone]: [Noises1.ogg]
    [ro.crypto.fs_crypto_blkdev]: [/dev/block/dm-1]
    [ro.crypto.state]: [encrypted]
    [ro.crypto.type]: [block]
    [ro.cust.def_brightness]: [127]
    [ro.cust.ril.defaultsupl]: [EUR]
    [ro.cust.ril.mms_max_size]: [300]
    [ro.cust.ril.nwmode_show4g]: [false]
    [ro.cust.ril.show4g]: [true]
    [ro.cust.ril.sms_max_pages]: [6]
    [ro.dalvik.vm.native.bridge]: [0]
    [ro.debuggable]: [0]
    [ro.expect.recovery_id]: [0x1030ea08f24a580f2c7035b832918d19c9bc521a000000000000000000000000]
    [ro.frp.pst]: [/dev/block/platform/mtk-msdc.0/11230000.msdc0/by-name/frp]
    [ro.hardware]: [mt6757]
    [ro.have_aacencode_feature]: [1]
    [ro.have_aee_feature]: [1]
    [ro.kernel.zio]: [38,108,105,16]
    [ro.media.maxmem]: [500000000]
    [ro.mediatek.chip_ver]: [S01]
    [ro.mediatek.platform]: [MT6757]
    [ro.mediatek.project.path]: [device/cci/cci6757_65_n]
    [ro.mediatek.version.branch]: [alps-mp-n0.mp5]
    [ro.mediatek.version.release]: [alps-mp-n0.mp5-V1_cci6757.65.n_P45]
    [ro.mediatek.version.sdk]: [4]
    [ro.mediatek.wlan.p2p]: [1]
    [ro.mediatek.wlan.wsc]: [1]
    [ro.mount.fs]: [EXT4]
    [ro.mtk_aal_support]: [1]
    [ro.mtk_afw_support]: [1]
    [ro.mtk_agps_app]: [1]
    [ro.mtk_audio_tuning_tool_ver]: [V2.2]
    [ro.mtk_besloudness_support]: [1]
    [ro.mtk_bg_power_saving_support]: [1]
    [ro.mtk_bg_power_saving_ui]: [1]
    [ro.mtk_bip_scws]: [1]
    [ro.mtk_blulight_def_support]: [1]
    [ro.mtk_bt_support]: [1]
    [ro.mtk_cam_lomo_support]: [1]
    [ro.mtk_cam_mfb_support]: [0]
    [ro.mtk_deinterlace_support]: [1]
    [ro.mtk_dhcpv6c_wifi]: [1]
    [ro.mtk_dialer_search_support]: [1]
    [ro.mtk_dual_mic_support]: [1]
    [ro.mtk_eap_sim_aka]: [1]
    [ro.mtk_emmc_support]: [1]
    [ro.mtk_enable_md1]: [1]
    [ro.mtk_external_sim_only_slots]: [0]
    [ro.mtk_fd_support]: [1]
    [ro.mtk_fm_50khz_support]: [1]
    [ro.mtk_gps_support]: [1]
    [ro.mtk_is_tablet]: [0]
    [ro.mtk_log_hide_gps]: [0]
    [ro.mtk_lte_support]: [1]
    [ro.mtk_md_sbp_custom_value]: [5]
    [ro.mtk_md_world_mode_support]: [1]
    [ro.mtk_microtrust_tee_support]: [1]
    [ro.mtk_miravision_support]: [1]
    [ro.mtk_modem_monitor_support]: [1]
    [ro.mtk_oma_drm_support]: [1]
    [ro.mtk_omacp_support]: [1]
    [ro.mtk_perf_fast_start_win]: [1]
    [ro.mtk_perf_response_time]: [1]
    [ro.mtk_perf_simple_start_win]: [1]
    [ro.mtk_perfservice_support]: [1]
    [ro.mtk_pow_perf_support]: [1]
    [ro.mtk_pq_color_mode]: [1]
    [ro.mtk_pq_support]: [2]
    [ro.mtk_protocol1_rat_config]: [Lf/W/G]
    [ro.mtk_rild_read_imsi]: [1]
    [ro.mtk_search_db_support]: [1]
    [ro.mtk_send_rr_support]: [1]
    [ro.mtk_shared_sdcard]: [1]
    [ro.mtk_sim_hot_swap]: [1]
    [ro.mtk_sim_hot_swap_common_slot]: [1]
    [ro.mtk_slow_motion_support]: [1]
    [ro.mtk_tetheringipv6_support]: [1]
    [ro.mtk_vilte_ut_support]: [0]
    [ro.mtk_wapi_support]: [1]
    [ro.mtk_wappush_support]: [1]
    [ro.mtk_wfd_support]: [1]
    [ro.mtk_widevine_drm_l3_support]: [1]
    [ro.mtk_wifi_mcc_support]: [1]
    [ro.mtk_wlan_support]: [1]
    [ro.mtk_world_phone_policy]: [0]
    [ro.mtk_zsdhdr_support]: [1]
    [ro.nfc.port]: [I2C]
    [ro.num_md_protocol]: [2]
    [ro.oem_unlock_supported]: [1]
    [ro.opengles.version]: [196610]
    [ro.operator.optr]: [EUR]
    [ro.product.board]: [mt6757]
    [ro.product.brand]: [Cat]
    [ro.product.cpu.abi]: [arm64-v8a]
    [ro.product.cpu.abilist]: [arm64-v8a,armeabi-v7a,armeabi]
    [ro.product.cpu.abilist32]: [armeabi-v7a,armeabi]
    [ro.product.cpu.abilist64]: [arm64-v8a]
    [ro.product.device]: [CatS41]
    [ro.product.first_api_level]: [24]
    [ro.product.locale]: [en-US]
    [ro.product.manufacturer]: [BullittGroupLimited]
    [ro.product.model]: [S41]
    [ro.product.name]: [CatS41]
    [ro.radio.version]: [LTE_D0201121.1_S41]
    [ro.recovery_id]: [0x1030ea08f24a580f2c7035b832918d19c9bc521a000000000000000000000000]
    [ro.revision]: [0]
    [ro.runtime.firstboot]: [1507104655335]
    [ro.secure]: [1]
    [ro.serialno]: [S411719005315]
    [ro.setupwizard.mode]: [OPTIONAL]
    [ro.setupwizard.require_network]: [no]
    [ro.sf.hwrotation]: [0]
    [ro.sf.lcd_density]: [420]
    [ro.sim_me_lock_mode]: [0]
    [ro.sim_refresh_reset_by_modem]: [1]
    [ro.sys.sdcardfs]: [1]
    [ro.sys.usb.bicr]: [no]
    [ro.sys.usb.charging.only]: [yes]
    [ro.sys.usb.mtp.whql.enable]: [0]
    [ro.sys.usb.storage.type]: [mtp]
    [ro.telephony.default_network]: [9,9]
    [ro.telephony.sim.count]: [2]
    [ro.wifi.channels]: []
    [ro.wlan.mtk.wifi.5g]: [1]
    [ro.zygote]: [zygote64_32]
    [ro.zygote.preload.enable]: [0]
    [security.perf_harden]: [1]
    [selinux.reload_policy]: [1]
    [service.bootanim.exit]: [1]
    [service.nvram_init]: [Ready]
    [service.wcn.coredump.mode]: [0]
    [service.wcn.driver.ready]: [yes]
    [soter.encrypt.state]: [OK]
    [soter.teei.init]: [INIT_OK]
    [soter.teei.vold.decrypt]: [OK]
    [sys.audio.gain.version]: [S41_20170810_1500]
    [sys.audio.smartpa.version]: [S41_20170808_1200]
    [sys.boot_completed]: [1]
    [sys.cei.powerbank]: [0]
    [sys.ipo.pwrdncap]: [2]
    [sys.ipowin.done]: [1]
    [sys.leds.reset]: [0]
    [sys.lowstorage_flag]: [0]
    [sys.oem_unlock_allowed]: [0]
    [sys.sysctl.extra_free_kbytes]: [24300]
    [sys.sysctl.tcp_def_init_rwnd]: [60]
    [sys.usb.config]: [mtp,adb]
    [sys.usb.configfs]: [0]
    [sys.usb.ffs.ready]: [1]
    [sys.usb.state]: [mtp,adb]
    [sys.usb.vid]: [04B7]
    [vold.decrypt]: [trigger_restart_framework]
    [vold.emmc_size]: [31268536320]
    [vold.encryption.type]: [default]
    [vold.has_adoptable]: [1]
    [vold.path.internal_storage]: [/storage/emulated/0]
    [vold.post_fs_data_done]: [1]
    [vold.support_external_sd]: [1]
    [wfd.dummy.enable]: [1]
    [wfd.iframesize.level]: [0]
    [wifi.direct.interface]: [p2p0]
    [wifi.interface]: [wlan0]
    [wifi.tethering.interface]: [ap0]
    [wlan.driver.status]: [ok]
    [wlan.wfd.security.image]: [1]
""")

        getprop_output = adb.Adb()._get_prop()

        self.assertEqual(getprop_output['gsm.sim.operator.alpha'], 'vodafone UK')
        self.assertEqual(getprop_output['ro.build.flavor'], 'CatS41-user')
        self.assertEqual(getprop_output['ro.build.version.software'], 'LTE_D0201121.0_S41_0.023.01')
        self.assertEqual(getprop_output['ro.build.version.release'], '7.0')
        self.assertEqual(getprop_output['ro.product.manufacturer'], 'BullittGroupLimited')
        self.assertEqual(getprop_output['wlan.wfd.security.image'], '1')

    def test_get_imei(self):
        adb.get_stdout_from_adb_command = MagicMock(return_value="""
Result: Parcel(
  0x00000000: 00000000 0000000f 00350033 00380037 '........3.5.7.8.'
  0x00000010: 00360037 00380030 00300030 00370030 '7.6.0.8.0.0.0.7.'
  0x00000020: 00340034 00000038                   '4.4.8...        ')
        """)

        self.assertEqual(adb.Adb().get_imei(), '357876080007448')

        adb.get_stdout_from_adb_command = MagicMock(return_value="""Result: 
        Parcel(\r\n  0x00000000: 00000000 0000000f 00350033 00380037 '........3.5.7.8.'\r\n  
        0x00000010: 00360037 00380030 00300030 00370030 '7.6.0.8.0.0.0.7.'\r\n  
        0x00000020: 00340034 00000038                   '4.4.8...        ')\r\n""")

        self.assertEqual(adb.Adb().get_imei(), '357876080007448')


if __name__ == '__main__':
    unittest.main()