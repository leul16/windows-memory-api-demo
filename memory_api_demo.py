from ctypes import *
from ctypes.wintypes import *
import subprocess
import time

kernel32 = windll.kernel32

SIZE_T = c_size_t


def verify(result):
    if not result:
        raise WinError()


class _SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ('nLength', DWORD),
        ('lpSecurityDescriptor', LPVOID),
        ('bInheritHandle', BOOL)
    ]


class _STARTUPINFOA(Structure):
    _fields_ = [
        ('cb', DWORD),
        ('lpReserved', LPSTR),
        ('lpDesktop', LPSTR),
        ('lpTitle', LPSTR),
        ('dwX', DWORD),
        ('dwY', DWORD),
        ('dwXSize', DWORD),
        ('dwYSize', DWORD),
        ('dwXCountChars', DWORD),
        ('dwYCountChars', DWORD),
        ('dwFillAttribute', DWORD),
        ('dwFlags', DWORD),
        ('wShowWindow', WORD),
        ('cbReserved2', WORD),
        ('lpReserved2', LPBYTE),
        ('hStdInput', HANDLE),
        ('hStdOutput', HANDLE),
        ('hStdError', HANDLE)
    ]


class _PROCESS_INFORMATION(Structure):
    _fields_ = [
        ('hProcess', HANDLE),
        ('hThread', HANDLE),
        ('dwProcessId', DWORD),
        ('dwThreadId', DWORD)
    ]


CreateProcessA = kernel32.CreateProcessA
CreateProcessA.argtypes = (
    LPCSTR,
    LPSTR,
    POINTER(_SECURITY_ATTRIBUTES),
    POINTER(_SECURITY_ATTRIBUTES),
    BOOL,
    DWORD,
    LPVOID,
    LPCSTR,
    POINTER(_STARTUPINFOA),
    POINTER(_PROCESS_INFORMATION)
)
CreateProcessA.restype = BOOL


GetModuleHandleA = kernel32.GetModuleHandleA
GetModuleHandleA.argtypes = (LPCSTR,)
GetModuleHandleA.restype = HANDLE


GetProcAddress = kernel32.GetProcAddress
GetProcAddress.argtypes = (HANDLE, LPCSTR)
GetProcAddress.restype = LPVOID


CREATE_NO_WINDOW = 0x08000000
Binary_Path = b'C:\\Windows\\System32\\notepad.exe'


StartupInfo = _STARTUPINFOA()
ProcessInfo = _PROCESS_INFORMATION()

StartupInfo.cb = sizeof(_STARTUPINFOA)

Process = CreateProcessA(
    Binary_Path,
    None,
    None,
    None,
    False,
    CREATE_NO_WINDOW,
    None,
    None,
    byref(StartupInfo),
    byref(ProcessInfo)
)

verify(Process)

print(
    f'Process Created with handle => {ProcessInfo.hProcess}, '
    f'PID => {ProcessInfo.dwProcessId}'
)

Kernel32_Handle = GetModuleHandleA(b'kernel32.dll')
verify(Kernel32_Handle)

print(f'Kernel32 Handle => {hex(Kernel32_Handle)}')

VirtualAlloc_Address = GetProcAddress(
    Kernel32_Handle,
    b'VirtualAllocEx'
)

verify(VirtualAlloc_Address)

print(
    f'VirtualAllocEx Address => {hex(VirtualAlloc_Address)}'
)

WriteMemory_Address = GetProcAddress(
    Kernel32_Handle,
    b'WriteProcessMemory'
)

verify(WriteMemory_Address)

print(
    f'WriteProcessMemory Address => {hex(WriteMemory_Address)}'
)

kernel32.TerminateProcess(ProcessInfo.hProcess, 0)

print('Process closed.')
