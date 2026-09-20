## Hi, I'm hsdfat 👋

Go engineer working on **telecom core networks** and the cloud-native
infrastructure they run on. Most of my time goes to mobile-core network
functions; the rest goes upstream, into the Kubernetes, storage, and
observability tools I depend on.

---

### 🛰️ What I'm building — `udm-system`

A Go monorepo implementing a combined **5GC + EPC core stack** — one service
per 3GPP network function, deployed to Kubernetes via Helm.

| Layer | Components |
|---|---|
| **5G core** | UDM, AUSF, UDR, context-management, provision |
| **EPC / legacy interworking** | HSS, EIR, Diameter gateway (S6a / Cx / Sh) |
| **Edge** | HTTP/2 SBI gateway, NETCONF control plane |
| **Data** | Distributed SQL backend, event-log and trace pipeline |
| **Tooling** | End-to-end test harness, performance and overload profilers |

Interesting parts: Per-function Go modules with shared crypto/database/diameter
libraries, 3GPP-aligned SBI request validation, Diameter↔HTTP protocol
translation, and load-testing tools built to find the overload cliff before
production does.

---

### 🌍 Open Source Contributions

I contribute upstream fixes to the Go infrastructure I run in production —
storage, Kubernetes tooling, policy engines, stream processors, and 5G core
projects.

<!-- OSS-STATS:START -->

**28 merged pull requests** across **14 upstream projects** totalling **230.3k stars** · **21** in review

### Merged

| Project | ★ | PR | Contribution |
|---|---:|---|---|
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9693](https://github.com/rclone/rclone/pull/9693) | fserrors: make http2 "server sent GOAWAY" a retriable error - fixes #96… |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9751](https://github.com/rclone/rclone/pull/9751) | operations: check checksums in rcat with known size - fixes #6305 |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9868](https://github.com/rclone/rclone/pull/9868) | dropbox: fix shared folder mount for roots nested more than one level d… |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9869](https://github.com/rclone/rclone/pull/9869) | dropbox: match shared-folder and received-file names case-insensitively |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9870](https://github.com/rclone/rclone/pull/9870) | serve docker: fix volume path being lost when the plugin restarts |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9872](https://github.com/rclone/rclone/pull/9872) | fs/config: only run --password-command once when using --daemon |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | 58.1k | [#38693](https://github.com/go-gitea/gitea/pull/38693) | fix(lfs): failed upload deletes a concurrent upload's meta object |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 38k | [#501](https://github.com/alibaba/open-code-review/pull/501) | feat(allowlist): add Julia (.jl) support |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 34.8k | [#10656](https://github.com/seaweedfs/seaweedfs/pull/10656) | s3api: fix ListObjectsV2 dropping objects under a partial prefix |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 34.8k | [#11393](https://github.com/seaweedfs/seaweedfs/pull/11393) | fix(volume): return an error instead of panicking on a corrupt needle s… |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 34.8k | [#11397](https://github.com/seaweedfs/seaweedfs/pull/11397) | fix(volume): return an error instead of 201 when a write lands on no vo… |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 34.8k | [#11398](https://github.com/seaweedfs/seaweedfs/pull/11398) | fix(volume): stop ScanVolumeFileFrom at a header it cannot advance past |
| [seaweedfs/seaweedfs](https://github.com/seaweedfs/seaweedfs) | 34.8k | [#11399](https://github.com/seaweedfs/seaweedfs/pull/11399) | fix(volume): validate sizes in ReadNeedleBlob and WriteNeedleBlob |
| [grpc-ecosystem/grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) | 20k | [#7110](https://github.com/grpc-ecosystem/grpc-gateway/pull/7110) | docs: add runnable OpenTelemetry tracing example |
| [grpc-ecosystem/grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) | 20k | [#7207](https://github.com/grpc-ecosystem/grpc-gateway/pull/7207) | fix(openapiv2): omit oneof siblings of path parameters from query param… |
| [shirou/gopsutil](https://github.com/shirou/gopsutil) | 11.9k | [#2143](https://github.com/shirou/gopsutil/pull/2143) | [docker][linux]: support cgroup v2 in Cgroup* functions |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1414](https://github.com/uptrace/bun/pull/1414) | fix(bunotel): honor WithMeterProvider when reporting DB stats metrics |
| [uptrace/bun](https://github.com/uptrace/bun) | 5k | [#1415](https://github.com/uptrace/bun/pull/1415) | fix(relation): do not duplicate joined models on a shared base model |
| [nginx/nginx-gateway-fabric](https://github.com/nginx/nginx-gateway-fabric) | 1.2k | [#5639](https://github.com/nginx/nginx-gateway-fabric/pull/5639) | fix: correct validation error diagnostics and add missing CRD schema co… |
| [bluenviron/gortsplib](https://github.com/bluenviron/gortsplib) | 939 | [#1171](https://github.com/bluenviron/gortsplib/pull/1171) | sdp: support oversized numbers in origin (bluenviron/mediamtx#5949) |
| [kerlenton/mcpsnoop](https://github.com/kerlenton/mcpsnoop) | 354 | [#212](https://github.com/kerlenton/mcpsnoop/pull/212) | feat(check): emit SARIF 2.1.0 so findings land in the Security tab |
| [kerlenton/mcpsnoop](https://github.com/kerlenton/mcpsnoop) | 354 | [#213](https://github.com/kerlenton/mcpsnoop/pull/213) | feat(cli): wrap and unwrap the Claude Desktop config for one server |
| [nickvsnetworking/pyhss](https://github.com/nickvsnetworking/pyhss) | 115 | [#337](https://github.com/nickvsnetworking/pyhss/pull/337) | diameterService: iterate over a snapshot of activePeers |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 98 | [#368](https://github.com/bluenviron/mediacommon/pull/368) | h265: fix DTS extraction of streams with temporal sub-layers |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 98 | [#373](https://github.com/bluenviron/mediacommon/pull/373) | pmp4: support stsz with a constant sample size (bluenviron/mediamtx#580… |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 98 | [#375](https://github.com/bluenviron/mediacommon/pull/375) | pmp4: support tracks without edts |
| [free5gc/amf](https://github.com/free5gc/amf) | 23 | [#232](https://github.com/free5gc/amf/pull/232) | fix: guard non-string DNN type assertions in GMM handler |
| [free5gc/tngf](https://github.com/free5gc/tngf) | 5 | [#47](https://github.com/free5gc/tngf/pull/47) | fix: prevent slice-bounds panic on malformed IKE SA proposal |

### In review

| Project | ★ | PR | Contribution |
|---|---:|---|---|
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9944](https://github.com/rclone/rclone/pull/9944) | operations: make --immutable work with copyto, moveto and single file c… |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9945](https://github.com/rclone/rclone/pull/9945) | smb: save the user name in the config even if it matches the current us… |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9946](https://github.com/rclone/rclone/pull/9946) | serve sftp, serve webdav: fix stale hashes reported while a file is bei… |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9947](https://github.com/rclone/rclone/pull/9947) | local: stop --copy-links following symlink loops - fixes #4402 |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9949](https://github.com/rclone/rclone/pull/9949) | vfs: fix AddVirtual ignoring isDir |
| [rclone/rclone](https://github.com/rclone/rclone) | 59.9k | [#9950](https://github.com/rclone/rclone/pull/9950) | serve dlna: log unescaped paths - fixes #7370 |
| [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) | 20.2k | [#6195](https://github.com/bluenviron/mediamtx/pull/6195) | playback: cache segment headers to speed up /list (#5094) |
| [bluenviron/mediamtx](https://github.com/bluenviron/mediamtx) | 20.2k | [#6196](https://github.com/bluenviron/mediamtx/pull/6196) | add udpWriteBufferSize parameter (#6100) |
| [argoproj/argo-workflows](https://github.com/argoproj/argo-workflows) | 17k | [#16602](https://github.com/argoproj/argo-workflows/pull/16602) | perf(executor): read the resource once for all output parameters. |
| [IBM/sarama](https://github.com/IBM/sarama) | 12.5k | [#3752](https://github.com/IBM/sarama/pull/3752) | fix(client): only deregister the broker registered under that ID |
| [IBM/sarama](https://github.com/IBM/sarama) | 12.5k | [#3753](https://github.com/IBM/sarama/pull/3753) | fix(offset): don't block PartitionOffsetManager.Close without auto-comm… |
| [kubeshark/kubeshark](https://github.com/kubeshark/kubeshark) | 12.1k | [#1956](https://github.com/kubeshark/kubeshark/pull/1956) | helm: use Recreate strategy for hub Deployment when local snapshots PVC… |
| [velero-io/velero](https://github.com/velero-io/velero) | 10.3k | [#10212](https://github.com/velero-io/velero/pull/10212) | Fix Zip Slip path check accepting a sibling directory in archive extrac… |
| [anchore/syft](https://github.com/anchore/syft) | 9.6k | [#5121](https://github.com/anchore/syft/pull/5121) | fix(binary): match istio snapshot and older pre-release versions |
| [redpanda-data/connect](https://github.com/redpanda-data/connect) | 8.8k | [#4656](https://github.com/redpanda-data/connect/pull/4656) | slack: only enforce token prefixes on literal values |
| [nickvsnetworking/pyhss](https://github.com/nickvsnetworking/pyhss) | 115 | [#338](https://github.com/nickvsnetworking/pyhss/pull/338) | diameter: answer with an error Result-Code when a handler raises |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 98 | [#376](https://github.com/bluenviron/mediacommon/pull/376) | pmp4: return seek errors from GetPayload |
| [bluenviron/mediacommon](https://github.com/bluenviron/mediacommon) | 98 | [#377](https://github.com/bluenviron/mediacommon/pull/377) | pmp4: support tracks longer than 2^32 ticks |
| [free5gc/udm](https://github.com/free5gc/udm) | 9 | [#96](https://github.com/free5gc/udm/pull/96) | fix(udm): return ProblemDetails for unmatched resource URIs |
| [free5gc/udr](https://github.com/free5gc/udr) | 4 | [#70](https://github.com/free5gc/udr/pull/70) | fix: return ProblemDetails for unmatched resource URIs |
| [free5gc/ike](https://github.com/free5gc/ike) | 3 | [#24](https://github.com/free5gc/ike/pull/24) | fix: prevent slice-bounds panics from uint8 SPI offset overflow |

<!-- OSS-STATS:END -->

<sub>Table regenerated nightly from the GitHub API by
[`scripts/build_stats.py`](scripts/build_stats.py) — own repositories excluded,
so every row is an upstream contribution.</sub>

---

### 🧰 Tech

`Go` · `Kubernetes` · `Helm` · `Docker` · `Diameter` · `HTTP/2 · SBI` ·
`NETCONF` · `gRPC / protobuf` · `distributed SQL` · `eBPF-adjacent tooling`

---

<p align="left">
  <img height="150" alt="hsdfat's GitHub stats"
       src="https://github-readme-stats.vercel.app/api?username=hsdfat&show_icons=true&hide_border=true&include_all_commits=true&theme=transparent" />
  <img height="150" alt="Top languages"
       src="https://github-readme-stats.vercel.app/api/top-langs/?username=hsdfat&layout=compact&hide_border=true&langs_count=6&theme=transparent" />
</p>

<sub>The cards above reflect activity in my own repositories only — the upstream
work is in the table above.</sub>
