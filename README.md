## Hi, I'm hsdfat 👋

Go engineer building **telecom core networks** and the cloud-native systems
around them. I work primarily on 5G/EPC network functions, then take the
production problems I find upstream to the Go and Kubernetes ecosystem.

### Focus

- 5G Core, EPC interworking, Diameter, SBI, HTTP/2, and NETCONF
- Go services on Kubernetes, with Helm-based delivery and end-to-end testing
- Storage, observability, and performance work that makes production systems
  safer under load

### Current work — `udm-system`

A Go monorepo for a combined 5GC + EPC stack: UDM, AUSF, UDR, HSS, EIR,
Diameter and HTTP/2 gateways, provisioning, and the test and profiling tools
needed to operate them.

### Open source

I contribute production-driven fixes to the infrastructure I use: Kubernetes
tooling, storage, media, observability, stream processing, and 5G projects.

<!-- OSS-STATS:START -->

**50 merged pull requests** (1 later reverted) across **24 upstream projects** totalling **285.9k stars** · **25** in review

<details>
<summary>Browse every merged and open upstream pull request</summary>

### Merged

| Project | ★ | PR | Contribution |
|---|---:|---|---|
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9693](https://github.com/rclone/rclone/pull/9693) | fserrors: make http2 "server sent GOAWAY" a retriable error - fixes #96… |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9751](https://github.com/rclone/rclone/pull/9751) | operations: check checksums in rcat with known size - fixes #6305 |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9868](https://github.com/rclone/rclone/pull/9868) | dropbox: fix shared folder mount for roots nested more than one level d… |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9869](https://github.com/rclone/rclone/pull/9869) | dropbox: match shared-folder and received-file names case-insensitively |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9870](https://github.com/rclone/rclone/pull/9870) | serve docker: fix volume path being lost when the plugin restarts |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9872](https://github.com/rclone/rclone/pull/9872) | fs/config: only run --password-command once when using --daemon |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9944](https://github.com/rclone/rclone/pull/9944) | operations: make --immutable work with copyto, moveto and single file c… |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9945](https://github.com/rclone/rclone/pull/9945) | smb: save the user name in the config even if it matches the current us… |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9947](https://github.com/rclone/rclone/pull/9947) | local: stop --copy-links following symlink loops - fixes #4402 |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9949](https://github.com/rclone/rclone/pull/9949) | vfs: fix AddVirtual ignoring isDir |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9950](https://github.com/rclone/rclone/pull/9950) | serve dlna: log unescaped paths - fixes #7370 |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9977](https://github.com/rclone/rclone/pull/9977) | docker: add mailcap for /etc/mime.types - fixes #6384 |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | 58.3k | [#38693](https://github.com/go-gitea/gitea/pull/38693) | fix(lfs): failed upload deletes a concurrent upload's meta object |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 44.1k | [#501](https://github.com/alibaba/open-code-review/pull/501) | feat(allowlist): add Julia (.jl) support |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 35.3k | [#10656](https://github.com/seaweedfs/seaweedfs/pull/10656) | s3api: fix ListObjectsV2 dropping objects under a partial prefix |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 35.3k | [#11393](https://github.com/seaweedfs/seaweedfs/pull/11393) | fix(volume): return an error instead of panicking on a corrupt needle s… |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 35.3k | [#11397](https://github.com/seaweedfs/seaweedfs/pull/11397) | fix(volume): return an error instead of 201 when a write lands on no vo… |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 35.3k | [#11398](https://github.com/seaweedfs/seaweedfs/pull/11398) | fix(volume): stop ScanVolumeFileFrom at a header it cannot advance past |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 35.3k | [#11399](https://github.com/seaweedfs/seaweedfs/pull/11399) | fix(volume): validate sizes in ReadNeedleBlob and WriteNeedleBlob |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 35.3k | [#11483](https://github.com/seaweedfs/seaweedfs/pull/11483) | fix(volume-rust): reserve a disk before replacing a replica in VolumeCo… |
| [grpc-ecosystem/grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) | 20k | [#7110](https://github.com/grpc-ecosystem/grpc-gateway/pull/7110) | docs: add runnable OpenTelemetry tracing example |
| [grpc-ecosystem/grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) | 20k | [#7207](https://github.com/grpc-ecosystem/grpc-gateway/pull/7207) | fix(openapiv2): omit oneof siblings of path parameters from query param… |
| [IBM/sarama](https://github.com/IBM/sarama) | 12.5k | [#3752](https://github.com/IBM/sarama/pull/3752) | fix(client): only deregister the broker registered under that ID |
| [kubeshark/kubeshark](https://github.com/kubeshark/kubeshark) | 12.1k | [#1956](https://github.com/kubeshark/kubeshark/pull/1956) | helm: use Recreate strategy for hub Deployment when local snapshots PVC… |
| [shirou/gopsutil](https://github.com/shirou/gopsutil) | 11.9k | [#2143](https://github.com/shirou/gopsutil/pull/2143) | [docker][linux]: support cgroup v2 in Cgroup* functions |
| [shirou/gopsutil](https://github.com/shirou/gopsutil) | 11.9k | [#2163](https://github.com/shirou/gopsutil/pull/2163) | [cpu][darwin]: don't crash in getFrequency when pmgr lacks voltage-stat… |
| [velero-io/velero](https://github.com/velero-io/velero) | 10.3k | [#10212](https://github.com/velero-io/velero/pull/10212) | Fix Zip Slip path check accepting a sibling directory in archive extrac… |
| [woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker) | 8k | [#7192](https://github.com/woodpecker-ci/woodpecker/pull/7192) | Fix race condition on concurrent pipeline config persist |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1414](https://github.com/uptrace/bun/pull/1414) | fix(bunotel): honor WithMeterProvider when reporting DB stats metrics |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1415](https://github.com/uptrace/bun/pull/1415) | fix(relation): do not duplicate joined models on a shared base model |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1435](https://github.com/uptrace/bun/pull/1435) | fix: resolve map column types before scanning rows |
| [apache/arrow-rs](https://github.com/apache/arrow-rs) | 3.6k | [#11229](https://github.com/apache/arrow-rs/pull/11229) | fix(parquet): support non-primitive map keys in record reader |
| [nginx/nginx-gateway-fabric](https://github.com/nginx/nginx-gateway-fabric) | 1.2k | [#5639](https://github.com/nginx/nginx-gateway-fabric/pull/5639) | fix: correct validation error diagnostics and add missing CRD schema co… |
| [bluenviron/gortsplib](https://github.com/bluenviron/gortsplib) | 941 | [#1171](https://github.com/bluenviron/gortsplib/pull/1171) | sdp: support oversized numbers in origin (bluenviron/mediamtx#5949) |
| [algesten/str0m](https://github.com/algesten/str0m) | 634 | [#1058](https://github.com/algesten/str0m/pull/1058) | Limit pacer burst size at high bitrates |
| [ClickHouse/clickhouse-rs](https://github.com/ClickHouse/clickhouse-rs) | 560 | [#478](https://github.com/ClickHouse/clickhouse-rs/pull/478) | fix(types): parse JSON type hints with parenthesized types |
| [ClickHouse/clickhouse-rs](https://github.com/ClickHouse/clickhouse-rs) | 560 | [#481](https://github.com/ClickHouse/clickhouse-rs/pull/481) | fix: use a derived query ID for insert schema lookups |
| [kerlenton/mcpsnoop](https://github.com/kerlenton/mcpsnoop) | 361 | [#212](https://github.com/kerlenton/mcpsnoop/pull/212) | feat(check): emit SARIF 2.1.0 so findings land in the Security tab |
| [kerlenton/mcpsnoop](https://github.com/kerlenton/mcpsnoop) | 361 | [#213](https://github.com/kerlenton/mcpsnoop/pull/213) | feat(cli): wrap and unwrap the Claude Desktop config for one server |
| [gopacket/gopacket](https://github.com/gopacket/gopacket) | 316 | [#172](https://github.com/gopacket/gopacket/pull/172) | **Reverted after merge.** packet: set zeroCopy in NewZeroCopyPacketSource |
| [fiorix/go-diameter](https://github.com/fiorix/go-diameter) | 295 | [#262](https://github.com/fiorix/go-diameter/pull/262) | diam: key the Unmarshal AVP index by {Code, VendorID} |
| [nickvsnetworking/pyhss](https://github.com/nickvsnetworking/pyhss) | 115 | [#337](https://github.com/nickvsnetworking/pyhss/pull/337) | diameterService: iterate over a snapshot of activePeers |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 101 | [#368](https://github.com/bluenviron/mediacommon/pull/368) | h265: fix DTS extraction of streams with temporal sub-layers |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 101 | [#373](https://github.com/bluenviron/mediacommon/pull/373) | pmp4: support stsz with a constant sample size (bluenviron/mediamtx#580… |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 101 | [#375](https://github.com/bluenviron/mediacommon/pull/375) | pmp4: support tracks without edts |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 101 | [#376](https://github.com/bluenviron/mediacommon/pull/376) | pmp4: return seek errors from GetPayload |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 101 | [#377](https://github.com/bluenviron/mediacommon/pull/377) | pmp4: support tracks longer than 2^32 ticks |
| [free5gc/amf](https://github.com/free5gc/amf) | 23 | [#232](https://github.com/free5gc/amf/pull/232) | fix: guard non-string DNN type assertions in GMM handler |
| [free5gc/tngf](https://github.com/free5gc/tngf) | 5 | [#47](https://github.com/free5gc/tngf/pull/47) | fix: prevent slice-bounds panic on malformed IKE SA proposal |
| [free5gc/ike](https://github.com/free5gc/ike) | 3 | [#24](https://github.com/free5gc/ike/pull/24) | fix: prevent slice-bounds panics from uint8 SPI offset overflow |

### In review

| Project | ★ | PR | Contribution |
|---|---:|---|---|
| [caddyserver/caddy](https://github.com/caddyserver/caddy) | 77.4k | [#8062](https://github.com/caddyserver/caddy/pull/8062) | caddyhttp: Add status_code option to http_redirect listener wrapper |
| [caddyserver/caddy](https://github.com/caddyserver/caddy) | 77.4k | [#8063](https://github.com/caddyserver/caddy/pull/8063) | caddyauth: Support third-party http.authentication.hashes modules |
| [rclone/rclone](https://github.com/rclone/rclone) | 60.2k | [#9946](https://github.com/rclone/rclone/pull/9946) | serve sftp, serve webdav: fix stale hashes reported while a file is bei… |
| [nushell/nushell](https://github.com/nushell/nushell) | 40.6k | [#19092](https://github.com/nushell/nushell/pull/19092) | Clear sqlite history with SQL instead of deleting the file |
| [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) | 20.4k | [#6195](https://github.com/bluenviron/mediamtx/pull/6195) | playback: cache segment headers to speed up /list (#5094) |
| [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) | 20.4k | [#6196](https://github.com/bluenviron/mediamtx/pull/6196) | add udpWriteBufferSize parameter (#6100) |
| [argoproj/argo-workflows](https://github.com/argoproj/argo-workflows) | 17k | [#16602](https://github.com/argoproj/argo-workflows/pull/16602) | perf(executor): read resource once for outputs (fixes #5658) |
| [IBM/sarama](https://github.com/IBM/sarama) | 12.5k | [#3753](https://github.com/IBM/sarama/pull/3753) | fix(offset): avoid deadlock when closing during a blocked commit |
| [anchore/syft](https://github.com/anchore/syft) | 9.6k | [#5121](https://github.com/anchore/syft/pull/5121) | fix(binary): match istio snapshot and older pre-release versions |
| [redpanda-data/connect](https://github.com/redpanda-data/connect) | 8.8k | [#4656](https://github.com/redpanda-data/connect/pull/4656) | slack: only enforce token prefixes on literal values |
| [woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker) | 8k | [#7189](https://github.com/woodpecker-ci/woodpecker/pull/7189) | Release agents waiting on long polls during server shutdown |
| [vishvananda/netlink](https://github.com/vishvananda/netlink) | 3.3k | [#1225](https://github.com/vishvananda/netlink/pull/1225) | filter: use EncDestIPMask when encoding Flower EncDestIP |
| [apache/iceberg-rust](https://github.com/apache/iceberg-rust) | 1.4k | [#3284](https://github.com/apache/iceberg-rust/pull/3284) | fix(spec): accept object-form partition-spec in manifest metadata |
| [bluenviron/gortsplib](https://github.com/bluenviron/gortsplib) | 941 | [#1178](https://github.com/bluenviron/gortsplib/pull/1178) | format: support mismatched fmtp payload type |
| [bluenviron/gortsplib](https://github.com/bluenviron/gortsplib) | 941 | [#1181](https://github.com/bluenviron/gortsplib/pull/1181) | client: support SETUP responses without Transport header |
| [pion/stun](https://github.com/pion/stun) | 861 | [#301](https://github.com/pion/stun/pull/301) | Restrict stun-client to IPv4 |
| [asticode/go-astits](https://github.com/asticode/go-astits) | 618 | [#79](https://github.com/asticode/go-astits/pull/79) | Sync to the first packet when the stream doesn't start with a sync byte |
| [pion/rtp](https://github.com/pion/rtp) | 478 | [#372](https://github.com/pion/rtp/pull/372) | Drop H264 FU-A fragments without a start |
| [scottlamb/retina](https://github.com/scottlamb/retina) | 374 | [#140](https://github.com/scottlamb/retina/pull/140) | H.265: treat all IRAP pictures (CRA/BLA) as random access points |
| [pion/interceptor](https://github.com/pion/interceptor) | 147 | [#470](https://github.com/pion/interceptor/pull/470) | Assign RTX sequence numbers at send time |
| [nickvsnetworking/pyhss](https://github.com/nickvsnetworking/pyhss) | 115 | [#338](https://github.com/nickvsnetworking/pyhss/pull/338) | diameter: answer with an error Result-Code when a handler raises |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 101 | [#380](https://github.com/bluenviron/mediacommon/pull/380) | mpegts: fix reading UDP datagrams larger than 1316 bytes |
| [free5gc/smf](https://github.com/free5gc/smf) | 25 | [#244](https://github.com/free5gc/smf/pull/244) | fix: release SMContext and reject when UDM token fetch fails |
| [free5gc/udm](https://github.com/free5gc/udm) | 9 | [#96](https://github.com/free5gc/udm/pull/96) | fix(udm): return ProblemDetails for unmatched resource URIs |
| [free5gc/udr](https://github.com/free5gc/udr) | 4 | [#70](https://github.com/free5gc/udr/pull/70) | fix: return ProblemDetails for unmatched resource URIs |

</details>

<!-- OSS-STATS:END -->

<sub>Regenerated nightly from the GitHub API by
[`scripts/build_stats.py`](scripts/build_stats.py). Own and private repositories
are excluded, so every row is a public upstream contribution.</sub>

### Tech

`Go` · `Kubernetes` · `Helm` · `Docker` · `gRPC / protobuf` · `Diameter` ·
`HTTP/2 · SBI` · `NETCONF` · `distributed SQL` · `observability`
