import os

def scale_lammps_data(input_path, output_path, scale_factor=0.999):
    with open(input_path, 'r') as f:
        lines = f.readlines()
    
    # 定位关键参数行
    xlo_line = next(i for i, line in enumerate(lines) if "xlo xhi" in line)
    ylo_line = next(i for i, line in enumerate(lines) if "ylo yhi" in line)
    tilt_line = next(i for i, line in enumerate(lines) if "xy xz yz" in line)
    atoms_start = next(i for i, line in enumerate(lines) if "Atoms" in line) + 2

    # 缩放盒子参数
    xlo, xhi = map(float, lines[xlo_line].split()[:2])
    lines[xlo_line] = f"{xlo*scale_factor:.15f} {xhi*scale_factor:.15f} xlo xhi\n"
    
    ylo, yhi = map(float, lines[ylo_line].split()[:2])
    lines[ylo_line] = f"{ylo*scale_factor:.15f} {yhi*scale_factor:.15f} ylo yhi\n"
    
    xy, xz, yz = map(float, lines[tilt_line].split()[:3])
    lines[tilt_line] = f"{xy*scale_factor:.15f} {xz} {yz} xy xz yz\n"

    # 缩放原子坐标
    for i in range(atoms_start, len(lines)):
        if not lines[i].strip() or lines[i].startswith('#'):
            continue
        parts = lines[i].split()
        if len(parts) >= 5:
            # 原子坐标在第三、四列 (0-based索引2,3)
            scaled_x = float(parts[2]) * scale_factor
            scaled_y = float(parts[3]) * scale_factor
            parts[2] = f"{scaled_x:.15f}"
            parts[3] = f"{scaled_y:.15f}"
            lines[i] = ' '.join(parts) + '\n'

    with open(output_path, 'w') as f:
        f.writelines(lines)

if __name__ == "__main__":
    input_file = "3_3.lmp"
    output_file = "scaled_struct.final"
    
    if os.path.exists(input_file):
        scale_lammps_data(input_file, output_file)
        print(f"生成文件: {output_file}")
    else:
        print(f"错误: {input_file} 不存在")