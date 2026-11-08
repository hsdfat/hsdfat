# Phat Le (hsdfat)

Go engineer working on telecom core networks (5G core and EPC) and the
Kubernetes systems around them. I build network functions for a living and
send the production bugs I hit upstream.

## Upstream contributions

<!-- OSS-STATS:START -->

**76 merged pull requests** (1 later reverted) across **33 upstream projects** totalling **449.6k stars** · **51** in review

<details>
<summary>Browse every merged and open upstream pull request</summary>

### Merged

| Project | ★ | PR | Contribution |
|---|---:|---|---|
| [caddyserver/caddy](https://github.com/caddyserver/caddy) | 78.9k | [#8063](https://github.com/caddyserver/caddy/pull/8063) | caddyauth: support third-party hash modules |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9693](https://github.com/rclone/rclone/pull/9693) | fserrors: make http2 "server sent GOAWAY" a retriable error - fixes #96… |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9751](https://github.com/rclone/rclone/pull/9751) | operations: check checksums in rcat with known size - fixes #6305 |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9868](https://github.com/rclone/rclone/pull/9868) | dropbox: fix shared folder mount for roots nested more than one level d… |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9869](https://github.com/rclone/rclone/pull/9869) | dropbox: match shared-folder and received-file names case-insensitively |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9870](https://github.com/rclone/rclone/pull/9870) | serve docker: fix volume path being lost when the plugin restarts |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9872](https://github.com/rclone/rclone/pull/9872) | fs/config: only run --password-command once when using --daemon |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9944](https://github.com/rclone/rclone/pull/9944) | operations: make --immutable work with copyto, moveto and single file c… |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9945](https://github.com/rclone/rclone/pull/9945) | smb: save the user name in the config even if it matches the current us… |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9947](https://github.com/rclone/rclone/pull/9947) | local: stop --copy-links following symlink loops - fixes #4402 |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9949](https://github.com/rclone/rclone/pull/9949) | vfs: fix AddVirtual ignoring isDir |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9950](https://github.com/rclone/rclone/pull/9950) | serve dlna: log unescaped paths - fixes #7370 |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9977](https://github.com/rclone/rclone/pull/9977) | docker: add mailcap for /etc/mime.types - fixes #6384 |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#10057](https://github.com/rclone/rclone/pull/10057) | lib/batcher: log when committing uploads has finished - fixes #5564 |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#10220](https://github.com/rclone/rclone/pull/10220) | serve sftp: fix rmdir deleting a file instead of returning an error |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#10221](https://github.com/rclone/rclone/pull/10221) | serve dlna: fix crash on Browse with a negative StartingIndex or Reques… |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | 59k | [#38693](https://github.com/go-gitea/gitea/pull/38693) | fix(lfs): failed upload deletes a concurrent upload's meta object |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 49.6k | [#501](https://github.com/alibaba/open-code-review/pull/501) | feat(allowlist): add Julia (.jl) support |
| [nushell/nushell](https://github.com/nushell/nushell) | 41.1k | [#19092](https://github.com/nushell/nushell/pull/19092) | Clear sqlite history with SQL instead of deleting the file |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 36k | [#10656](https://github.com/seaweedfs/seaweedfs/pull/10656) | s3api: fix ListObjectsV2 dropping objects under a partial prefix |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 36k | [#11393](https://github.com/seaweedfs/seaweedfs/pull/11393) | fix(volume): return an error instead of panicking on a corrupt needle s… |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 36k | [#11397](https://github.com/seaweedfs/seaweedfs/pull/11397) | fix(volume): return an error instead of 201 when a write lands on no vo… |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 36k | [#11398](https://github.com/seaweedfs/seaweedfs/pull/11398) | fix(volume): stop ScanVolumeFileFrom at a header it cannot advance past |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 36k | [#11399](https://github.com/seaweedfs/seaweedfs/pull/11399) | fix(volume): validate sizes in ReadNeedleBlob and WriteNeedleBlob |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 36k | [#11483](https://github.com/seaweedfs/seaweedfs/pull/11483) | fix(volume-rust): reserve a disk before replacing a replica in VolumeCo… |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 36k | [#12269](https://github.com/seaweedfs/seaweedfs/pull/12269) | fix(volume): reject a negative suffix length in Range headers |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 36k | [#12270](https://github.com/seaweedfs/seaweedfs/pull/12270) | fix(s3): reject non-integer max-parts, part-number-marker and max-uploa… |
| [grpc-ecosystem/grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) | 20k | [#7110](https://github.com/grpc-ecosystem/grpc-gateway/pull/7110) | docs: add runnable OpenTelemetry tracing example |
| [grpc-ecosystem/grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) | 20k | [#7207](https://github.com/grpc-ecosystem/grpc-gateway/pull/7207) | fix(openapiv2): omit oneof siblings of path parameters from query param… |
| [argoproj/argo-workflows](https://github.com/argoproj/argo-workflows) | 17.1k | [#16602](https://github.com/argoproj/argo-workflows/pull/16602) | perf(executor): read resource once for outputs (fixes #5658) |
| [IBM/sarama](https://github.com/IBM/sarama) | 12.5k | [#3752](https://github.com/IBM/sarama/pull/3752) | fix(client): only deregister the broker registered under that ID |
| [IBM/sarama](https://github.com/IBM/sarama) | 12.5k | [#3852](https://github.com/IBM/sarama/pull/3852) | fix(protocol): don't send an unclean election as ElectLeaders v0 |
| [kubeshark/kubeshark](https://github.com/kubeshark/kubeshark) | 12.1k | [#1956](https://github.com/kubeshark/kubeshark/pull/1956) | helm: use Recreate strategy for hub Deployment when local snapshots PVC… |
| [shirou/gopsutil](https://github.com/shirou/gopsutil) | 11.9k | [#2143](https://github.com/shirou/gopsutil/pull/2143) | [docker][linux]: support cgroup v2 in Cgroup* functions |
| [shirou/gopsutil](https://github.com/shirou/gopsutil) | 11.9k | [#2163](https://github.com/shirou/gopsutil/pull/2163) | [cpu][darwin]: don't crash in getFrequency when pmgr lacks voltage-stat… |
| [shirou/gopsutil](https://github.com/shirou/gopsutil) | 11.9k | [#2190](https://github.com/shirou/gopsutil/pull/2190) | [disk][linux]: decode only \ooo escapes in mount points |
| [shirou/gopsutil](https://github.com/shirou/gopsutil) | 11.9k | [#2191](https://github.com/shirou/gopsutil/pull/2191) | [net][linux]: fix IPv6 address decoding on big-endian hosts |
| [velero-io/velero](https://github.com/velero-io/velero) | 10.4k | [#10212](https://github.com/velero-io/velero/pull/10212) | Fix Zip Slip path check accepting a sibling directory in archive extrac… |
| [anchore/syft](https://github.com/anchore/syft) | 9.9k | [#5121](https://github.com/anchore/syft/pull/5121) | fix(binary): match istio snapshot and older pre-release versions |
| [woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker) | 8.1k | [#7189](https://github.com/woodpecker-ci/woodpecker/pull/7189) | Release agents waiting on long polls during server shutdown |
| [woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker) | 8.1k | [#7192](https://github.com/woodpecker-ci/woodpecker/pull/7192) | Fix race condition on concurrent pipeline config persist |
| [woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker) | 8.1k | [#7454](https://github.com/woodpecker-ci/woodpecker/pull/7454) | Fix image tag detection for registries with a port |
| [woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker) | 8.1k | [#7501](https://github.com/woodpecker-ci/woodpecker/pull/7501) | Return log store errors to the agent, except for duplicate entries |
| [webrtc-rs/webrtc](https://github.com/webrtc-rs/webrtc) | 5.2k | [#954](https://github.com/webrtc-rs/webrtc/pull/954) | fix(ice): use a random transaction ID for STUN Binding requests |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1414](https://github.com/uptrace/bun/pull/1414) | fix(bunotel): honor WithMeterProvider when reporting DB stats metrics |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1415](https://github.com/uptrace/bun/pull/1415) | fix(relation): do not duplicate joined models on a shared base model |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1435](https://github.com/uptrace/bun/pull/1435) | fix: resolve map column types before scanning rows |
| [apache/arrow-rs](https://github.com/apache/arrow-rs) | 3.7k | [#11229](https://github.com/apache/arrow-rs/pull/11229) | fix(parquet): support non-primitive map keys in record reader |
| [apache/arrow-rs](https://github.com/apache/arrow-rs) | 3.7k | [#12006](https://github.com/apache/arrow-rs/pull/12006) | fix(arrow-string): saturate the length in Utf8View/BinaryView substring |
| [apache/arrow-rs](https://github.com/apache/arrow-rs) | 3.7k | [#12007](https://github.com/apache/arrow-rs/pull/12007) | fix(arrow-json): reject out-of-range float timestamps instead of satura… |
| [apache/arrow-rs](https://github.com/apache/arrow-rs) | 3.7k | [#12108](https://github.com/apache/arrow-rs/pull/12108) | fix(parquet): return error on negative DELTA_BYTE_ARRAY lengths in arro… |
| [vishvananda/netlink](https://github.com/vishvananda/netlink) | 3.3k | [#1225](https://github.com/vishvananda/netlink/pull/1225) | filter: use EncDestIPMask when encoding Flower EncDestIP |
| [nginx/nginx-gateway-fabric](https://github.com/nginx/nginx-gateway-fabric) | 1.2k | [#5639](https://github.com/nginx/nginx-gateway-fabric/pull/5639) | fix: correct validation error diagnostics and add missing CRD schema co… |
| [bluenviron/gortsplib](https://github.com/bluenviron/gortsplib) | 944 | [#1171](https://github.com/bluenviron/gortsplib/pull/1171) | sdp: support oversized numbers in origin (bluenviron/mediamtx#5949) |
| [algesten/str0m](https://github.com/algesten/str0m) | 648 | [#1058](https://github.com/algesten/str0m/pull/1058) | Limit pacer burst size at high bitrates |
| [ClickHouse/clickhouse-rs](https://github.com/ClickHouse/clickhouse-rs) | 570 | [#478](https://github.com/ClickHouse/clickhouse-rs/pull/478) | fix(types): parse JSON type hints with parenthesized types |
| [ClickHouse/clickhouse-rs](https://github.com/ClickHouse/clickhouse-rs) | 570 | [#481](https://github.com/ClickHouse/clickhouse-rs/pull/481) | fix: use a derived query ID for insert schema lookups |
| [jonas-grgt/ktea](https://github.com/jonas-grgt/ktea) | 444 | [#179](https://github.com/jonas-grgt/ktea/pull/179) | feat: allow configuring the debug log location with --debug=PATH |
| [kerlenton/mcpsnoop](https://github.com/kerlenton/mcpsnoop) | 367 | [#212](https://github.com/kerlenton/mcpsnoop/pull/212) | feat(check): emit SARIF 2.1.0 so findings land in the Security tab |
| [kerlenton/mcpsnoop](https://github.com/kerlenton/mcpsnoop) | 367 | [#213](https://github.com/kerlenton/mcpsnoop/pull/213) | feat(cli): wrap and unwrap the Claude Desktop config for one server |
| [gopacket/gopacket](https://github.com/gopacket/gopacket) | 320 | [#172](https://github.com/gopacket/gopacket/pull/172) | **Reverted after merge.** packet: set zeroCopy in NewZeroCopyPacketSource |
| [fiorix/go-diameter](https://github.com/fiorix/go-diameter) | 298 | [#262](https://github.com/fiorix/go-diameter/pull/262) | diam: key the Unmarshal AVP index by {Code, VendorID} |
| [fiorix/go-diameter](https://github.com/fiorix/go-diameter) | 298 | [#276](https://github.com/fiorix/go-diameter/pull/276) | diam: keep only the P flag of the request in Answer |
| [pyhss/pyhss](https://github.com/pyhss/pyhss) | 114 | [#337](https://github.com/pyhss/pyhss/pull/337) | diameterService: iterate over a snapshot of activePeers |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 105 | [#368](https://github.com/bluenviron/mediacommon/pull/368) | h265: fix DTS extraction of streams with temporal sub-layers |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 105 | [#373](https://github.com/bluenviron/mediacommon/pull/373) | pmp4: support stsz with a constant sample size (bluenviron/mediamtx#580… |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 105 | [#375](https://github.com/bluenviron/mediacommon/pull/375) | pmp4: support tracks without edts |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 105 | [#376](https://github.com/bluenviron/mediacommon/pull/376) | pmp4: return seek errors from GetPayload |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 105 | [#377](https://github.com/bluenviron/mediacommon/pull/377) | pmp4: support tracks longer than 2^32 ticks |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 105 | [#398](https://github.com/bluenviron/mediacommon/pull/398) | h264: fix SPS width when ChromaArrayType is 0 |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 105 | [#399](https://github.com/bluenviron/mediacommon/pull/399) | av1: support sequence headers with initial display delay |
| [free5gc/amf](https://github.com/free5gc/amf) | 23 | [#232](https://github.com/free5gc/amf/pull/232) | fix: guard non-string DNN type assertions in GMM handler |
| [free5gc/udm](https://github.com/free5gc/udm) | 9 | [#96](https://github.com/free5gc/udm/pull/96) | fix(udm): return ProblemDetails for unmatched resource URIs |
| [free5gc/tngf](https://github.com/free5gc/tngf) | 5 | [#47](https://github.com/free5gc/tngf/pull/47) | fix: prevent slice-bounds panic on malformed IKE SA proposal |
| [free5gc/udr](https://github.com/free5gc/udr) | 4 | [#70](https://github.com/free5gc/udr/pull/70) | fix: return ProblemDetails for unmatched resource URIs |
| [free5gc/ike](https://github.com/free5gc/ike) | 3 | [#24](https://github.com/free5gc/ike/pull/24) | fix: prevent slice-bounds panics from uint8 SPI offset overflow |

### In review

| Project | ★ | PR | Contribution |
|---|---:|---|---|
| [caddyserver/caddy](https://github.com/caddyserver/caddy) | 78.9k | [#8062](https://github.com/caddyserver/caddy/pull/8062) | caddyhttp: Add status_code option to http_redirect listener wrapper |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#9946](https://github.com/rclone/rclone/pull/9946) | serve sftp, serve webdav: fix stale hashes reported while a file is bei… |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#10271](https://github.com/rclone/rclone/pull/10271) | fs: add --max-errors flag - fixes #4670 |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.9k | [#10279](https://github.com/rclone/rclone/pull/10279) | ls, lsl, lsd, lsf, lsjson: add --output-file flag - fixes #8358 |
| [wagoodman/dive](https://github.com/wagoodman/dive) | 54.7k | [#735](https://github.com/wagoodman/dive/pull/735) | fix: drop lower dir contents when a layer replaces the dir with a symli… |
| [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) | 20.6k | [#6447](https://github.com/bluenviron/mediamtx/pull/6447) | playback: limit parallel segment reads in /list (#6446) |
| [influxdata/telegraf](https://github.com/influxdata/telegraf) | 17.9k | [#20081](https://github.com/influxdata/telegraf/pull/20081) | feat(inputs.statsd): Add unixgram support |
| [influxdata/telegraf](https://github.com/influxdata/telegraf) | 17.9k | [#20085](https://github.com/influxdata/telegraf/pull/20085) | feat(inputs.jenkins): Add option to add build display name and descript… |
| [influxdata/telegraf](https://github.com/influxdata/telegraf) | 17.9k | [#20086](https://github.com/influxdata/telegraf/pull/20086) | feat(outputs.postgresql): Allow setting schema from a tag |
| [influxdata/telegraf](https://github.com/influxdata/telegraf) | 17.9k | [#20087](https://github.com/influxdata/telegraf/pull/20087) | feat(logging): Add syslog as log format |
| [influxdata/telegraf](https://github.com/influxdata/telegraf) | 17.9k | [#20088](https://github.com/influxdata/telegraf/pull/20088) | fix(common.opcua): Handle LocalizedText node values |
| [influxdata/telegraf](https://github.com/influxdata/telegraf) | 17.9k | [#20089](https://github.com/influxdata/telegraf/pull/20089) | feat(outputs.mqtt): Add last will and testament support |
| [swaggo/swag](https://github.com/swaggo/swag) | 13k | [#2239](https://github.com/swaggo/swag/pull/2239) | fix(v3): support title struct tag in OpenAPI 3.1 field parser |
| [IBM/sarama](https://github.com/IBM/sarama) | 12.5k | [#3753](https://github.com/IBM/sarama/pull/3753) | fix(offset): avoid deadlock when closing during a blocked commit |
| [IBM/sarama](https://github.com/IBM/sarama) | 12.5k | [#3851](https://github.com/IBM/sarama/pull/3851) | fix(protocol): decode compressed batches with more records than bytes |
| [redpanda-data/connect](https://github.com/redpanda-data/connect) | 8.8k | [#4656](https://github.com/redpanda-data/connect/pull/4656) | slack: only enforce token prefixes on literal values |
| [webrtc-rs/webrtc](https://github.com/webrtc-rs/webrtc) | 5.2k | [#955](https://github.com/webrtc-rs/webrtc/pull/955) | fix(ice): dial passive ICE-TCP candidates carried in the remote SDP |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1466](https://github.com/uptrace/bun/pull/1466) | fix: require primary keys for bulk UpdateQuery |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1467](https://github.com/uptrace/bun/pull/1467) | fix(pgdialect): scan int64 and float64 range bounds instead of panicking |
| [apache/arrow-rs](https://github.com/apache/arrow-rs) | 3.7k | [#12102](https://github.com/apache/arrow-rs/pull/12102) | fix(arrow-cast): write timestamps whose zone offset has seconds in UTC |
| [prometheus-community/postgres_exporter](https://github.com/prometheus-community/postgres_exporter) | 3.6k | [#1443](https://github.com/prometheus-community/postgres_exporter/pull/1443) | stat_wal_receiver: export metrics when replicating without a slot |
| [pdeljanov/Symphonia](https://github.com/pdeljanov/Symphonia) | 3.5k | [#608](https://github.com/pdeljanov/Symphonia/pull/608) | isomp4: Fix integer overflow in stts sample lookups. |
| [pdeljanov/Symphonia](https://github.com/pdeljanov/Symphonia) | 3.5k | [#609](https://github.com/pdeljanov/Symphonia/pull/609) | isomp4: Return an error instead of underflowing in MoofSegment sample l… |
| [pdeljanov/Symphonia](https://github.com/pdeljanov/Symphonia) | 3.5k | [#610](https://github.com/pdeljanov/Symphonia/pull/610) | isomp4: Return an error for a trun data offset outside the stream. |
| [pdeljanov/Symphonia](https://github.com/pdeljanov/Symphonia) | 3.5k | [#611](https://github.com/pdeljanov/Symphonia/pull/611) | ogg: Set packet DTS equal to PTS. |
| [vishvananda/netlink](https://github.com/vishvananda/netlink) | 3.3k | [#1237](https://github.com/vishvananda/netlink/pull/1237) | netkit: add PeerAttrs getter |
| [vishvananda/netlink](https://github.com/vishvananda/netlink) | 3.3k | [#1238](https://github.com/vishvananda/netlink/pull/1238) | Close subscribe sockets when the receive goroutine exits |
| [xerial/sqlite-jdbc](https://github.com/xerial/sqlite-jdbc) | 3.3k | [#1501](https://github.com/xerial/sqlite-jdbc/pull/1501) | fix(core): redact encryption key pragmas in trace logs |
| [pjsip/pjproject](https://github.com/pjsip/pjproject) | 2.7k | [#5384](https://github.com/pjsip/pjproject/pull/5384) | pjsua: make the maximum number of transports configurable |
| [obi1kenobi/cargo-semver-checks](https://github.com/obi1kenobi/cargo-semver-checks) | 1.7k | [#1797](https://github.com/obi1kenobi/cargo-semver-checks/pull/1797) | Add exported_function_now_variadic and exported_function_no_longer_vari… |
| [hyperium/h2](https://github.com/hyperium/h2) | 1.6k | [#1002](https://github.com/hyperium/h2/pull/1002) | fix: requeue released credit on recv window shrink |
| [apache/iceberg-rust](https://github.com/apache/iceberg-rust) | 1.4k | [#3645](https://github.com/apache/iceberg-rust/pull/3645) | fix(transform): avoid overflow in adjust_boundary at type extremes |
| [pion/stun](https://github.com/pion/stun) | 864 | [#301](https://github.com/pion/stun/pull/301) | Restrict stun-client to IPv4 |
| [JFryy/qq](https://github.com/JFryy/qq) | 739 | [#108](https://github.com/JFryy/qq/pull/108) | feat: add --indent flag to control output indentation |
| [algesten/str0m](https://github.com/algesten/str0m) | 648 | [#1128](https://github.com/algesten/str0m/pull/1128) | Allow setting msid via DirectApi |
| [algesten/str0m](https://github.com/algesten/str0m) | 648 | [#1129](https://github.com/algesten/str0m/pull/1129) | Remove native OpenSSL DTLS; use dimpl for the openssl backend |
| [asticode/go-astits](https://github.com/asticode/go-astits) | 617 | [#79](https://github.com/asticode/go-astits/pull/79) | Sync to the first packet when the stream doesn't start with a sync byte |
| [ClickHouse/clickhouse-rs](https://github.com/ClickHouse/clickhouse-rs) | 570 | [#507](https://github.com/ClickHouse/clickhouse-rs/pull/507) | feat: add Insert::set_buffer_size() |
| [ClickHouse/clickhouse-rs](https://github.com/ClickHouse/clickhouse-rs) | 570 | [#508](https://github.com/ClickHouse/clickhouse-rs/pull/508) | feat: support different column names for serialization and deserializat… |
| [ClickHouse/clickhouse-rs](https://github.com/ClickHouse/clickhouse-rs) | 570 | [#511](https://github.com/ClickHouse/clickhouse-rs/pull/511) | feat(serde): add `::vec` helpers for temporal types |
| [pion/rtp](https://github.com/pion/rtp) | 479 | [#372](https://github.com/pion/rtp/pull/372) | Drop H264 FU-A fragments without a start |
| [flock-php/flock](https://github.com/flock-php/flock) | 463 | [#116](https://github.com/flock-php/flock/pull/116) | fix(cli): respect ZDOTDIR when adding Flock to the zsh PATH |
| [gopacket/gopacket](https://github.com/gopacket/gopacket) | 320 | [#177](https://github.com/gopacket/gopacket/pull/177) | packet: copy zero copy data on the Packets channel path |
| [fiorix/go-diameter](https://github.com/fiorix/go-diameter) | 298 | [#275](https://github.com/fiorix/go-diameter/pull/275) | diam: match the Vendor-Id in FindAVP, FindAVPs and FindAVPsWithPath |
| [webrtc-rs/rtc](https://github.com/webrtc-rs/rtc) | 167 | [#314](https://github.com/webrtc-rs/rtc/pull/314) | fix(rtc): count incoming RTCP in get_stats() |
| [webrtc-rs/rtc](https://github.com/webrtc-rs/rtc) | 167 | [#315](https://github.com/webrtc-rs/rtc/pull/315) | fix(ice): answer USE-CANDIDATE checks without ICE-CONTROLLING on the co… |
| [webrtc-rs/rtc](https://github.com/webrtc-rs/rtc) | 167 | [#316](https://github.com/webrtc-rs/rtc/pull/316) | fix(turn): track client permissions per peer IP, not per IP and port |
| [webrtc-rs/rtc](https://github.com/webrtc-rs/rtc) | 167 | [#317](https://github.com/webrtc-rs/rtc/pull/317) | fix(ice): re-check a Failed pair when the remote's Binding request arri… |
| [pion/interceptor](https://github.com/pion/interceptor) | 149 | [#470](https://github.com/pion/interceptor/pull/470) | Assign RTX sequence numbers at send time |
| [pyhss/pyhss](https://github.com/pyhss/pyhss) | 114 | [#338](https://github.com/pyhss/pyhss/pull/338) | diameter: answer with an error Result-Code when a handler raises |
| [free5gc/smf](https://github.com/free5gc/smf) | 26 | [#244](https://github.com/free5gc/smf/pull/244) | fix: release SMContext and reject when UDM token fetch fails |

</details>

<!-- OSS-STATS:END -->

### Selected fixes

Hand-picked from the list above: fixes that stopped data loss, crashes, or
security problems in software a lot of people run.

| Project | Fix |
|---|---|
| [gitea #38693](https://github.com/go-gitea/gitea/pull/38693) | LFS: a failed upload no longer deletes a concurrent upload's metadata |
| [velero #10212](https://github.com/velero-io/velero/pull/10212) | Zip Slip check accepted a sibling directory during archive extraction |
| [rclone #9947](https://github.com/rclone/rclone/pull/9947) | `--copy-links` no longer follows symlink loops |
| [seaweedfs #11393](https://github.com/seaweedfs/seaweedfs/pull/11393) | Volume server returns an error instead of panicking on a corrupt needle |
| [sarama #3752](https://github.com/IBM/sarama/pull/3752) | Client only deregisters the broker registered under that ID |
| [argo-workflows #16602](https://github.com/argoproj/argo-workflows/pull/16602) | Executor reads the resource once when collecting outputs |
| [woodpecker #7192](https://github.com/woodpecker-ci/woodpecker/pull/7192) | Race on concurrent pipeline config persist |
| [gopsutil #2143](https://github.com/shirou/gopsutil/pull/2143) | cgroup v2 support in the `Cgroup*` functions |
| [webrtc-rs #954](https://github.com/webrtc-rs/webrtc/pull/954) | STUN Binding requests used an all-zero transaction ID |

## Projects

| Repository | What it is |
|---|---|
| [diam-gw](https://github.com/hsdfat/diam-gw) | Diameter gateway: client library and code generator, with CI and a performance budget |
| [go-eir](https://github.com/hsdfat/go-eir) | Equipment Identity Register (EIR) in Go, hexagonal architecture |
| [gohss](https://github.com/hsdfat/gohss) | HSS with S6a, Cx and Sh interfaces |
| [telco](https://github.com/hsdfat/telco) | Shared telecom utilities: 3GPP types, encoders, and test helpers |
| [go-project-dump](https://github.com/hsdfat/go-project-dump) | Dump a Go project into a single reviewable document |
| [go-auth-middleware](https://github.com/hsdfat/go-auth-middleware) | JWT authentication and role-based authorization middleware for Gin |

The combined 5GC + EPC stack I work on day to day (UDM, AUSF, UDR, HSS, EIR,
Diameter and HTTP/2 gateways) is private. The free5gc, go-diameter and PyHSS
fixes above come out of it.

## Focus

- 5G core and EPC interworking: SBI over HTTP/2, Diameter, NETCONF
- Go services on Kubernetes, delivered with Helm and end-to-end tests
- Storage, media and observability code paths that have to stay up under load

`Go` · `Rust` · `Kubernetes` · `Helm` · `gRPC` · `Diameter` · `HTTP/2` · `NETCONF` · `PostgreSQL` · `ClickHouse`

<sub>The contribution block is regenerated nightly by
[`scripts/build_stats.py`](scripts/build_stats.py); own and private
repositories are excluded, so every row is a public upstream pull request.</sub>
