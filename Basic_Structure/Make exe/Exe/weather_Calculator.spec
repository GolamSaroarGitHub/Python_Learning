# -*- mode: python -*-

block_cipher = None


a = Analysis(['weather_Calculator.py'],
             pathex=['F:\\Git\\Python_Learning\\Basic_Structure\\Make exe\\Exe'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='weather_Calculator',
          debug=False,
          strip=False,
          upx=True,
          console=True )
