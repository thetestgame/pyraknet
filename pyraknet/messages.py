"""
PyRakNet
Copyright (C) 2017 Stellar Gaming Network

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from enum import IntEnum

class Message(IntEnum):
    InternalPing = 0x00
    Ping = 0x01
    PingOpenConnections = 0x02
    ConnectedPong = 0x03
    ConnectionRequest = 0x04
    SecuredConnectionResponse = 0x05
    SecuredConnectionConfirmation = 0x06
    RPCMapping = 0x07
    DetectLostConnections = 0x08
    OpenConnectionRequest = 0x09
    OpenConnectionReply = 0x0a
    RPC = 0x0b
    RPCReply = 0x0c
    OutOfBandInternal = 0x0d
    ConnectionRequestAccepted = 0x0e
    ConnectionAttemptFailed = 0x0f
    AlreadyConnected = 0x10
    NewIncomingConnection = 0x11
    NoFreeIncomingConnections = 0x12
    DisconnectionNotification = 0x13
    ConnectionLost = 0x14
    RSAPublicKeyMismatch = 0x15
    ConnectionBanned = 0x16
    InvalidPassword = 0x17
    ModifiedPacket = 0x18
    Timestamp = 0x19
    Pong = 0x1a
    AdvertiseSystem = 0x1b
    RemoteDisconnectionNotification = 0x1c
    RemoteConnectionLost = 0x1d
    RemoteNewIncomingConnection = 0x1e
    DownloadProgress = 0x1f
    FileListTransferHeader = 0x20
    FileListTransferFile = 0x21
    DDTDownloadRequest = 0x22
    TransportString = 0x23
    ReplicaManagerConstruction = 0x24
    ReplicaManagerDestruction = 0x25
    ReplicaManagerScopeChange = 0x26
    ReplicaManagerSerialize = 0x27
    ReplicaManagerDownloadStarted = 0x28
    ReplicaManagerDownloadComplete = 0x29
    ConnectionGraphRequest = 0x2a
    ConnectionGraphReply = 0x2b
    ConnectionGraphUpdate = 0x2c
    ConnectionGraphNewConnection = 0x2d
    ConnectionGraphConnectionLost = 0x2e
    ConnectionGraphDisconnectionNotification = 0x2f
    RouteAndMulticast = 0x30
    RakvoiceOpenChannelRequest = 0x31
    RakvoiceOpenChannelReply = 0x32
    RakvoiceCloseChannel = 0x33
    RakvoiceData = 0x34
    AutopatcherGetChangelistSinceDate = 0x35
    AutopatcherCreationList = 0x36
    AutopatcherDeletionList = 0x37
    AutopatcherGetPatch = 0x38
    AutopatcherPatchList = 0x39
    AutopatcherRepositoryFatalError = 0x3a
    AutopatcherFinishedInternal = 0x3b
    AutopatcherFinished = 0x3c
    AutopatcherRestartApplication = 0x3d
    NATPunchthroughRequest = 0x3e
    NATTargetNotConnected = 0x3f
    NATTargetConnectionLost = 0x40
    NATConnectAtTime = 0x41
    NATSendOfflineMessageAtTime = 0x42
    NATInProgress = 0x43
    DatabaseQueryRequest = 0x44
    DatabaseUpdateRow = 0x45
    DatabaseRemoveRow = 0x46
    DatabaseQueryReply = 0x47
    DatabaseUnknownTable = 0x48
    DatabaseIncorrectPassword = 0x49
    ReadyEventSet = 0x4a
    ReadyEventUnset = 0x4b
    ReadyEventAllSet = 0x4c
    ReadyEventQuery = 0x4d
    LobbyGeneral = 0x4e
    AutoRPCCall = 0x4f
    AutoRPCRemoteIndex = 0x50
    AutoRPCUnknownRemoteIndex = 0x51
    RPCRemoteError = 0x52
